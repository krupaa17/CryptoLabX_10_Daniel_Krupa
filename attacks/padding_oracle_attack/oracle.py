import secrets
from collections.abc import Callable

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


BLOCK_SIZE = 16


def pkcs7_pad(data: bytes) -> bytes:
    padding_length = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding_length]) * padding_length


def pkcs7_unpad(data: bytes) -> bytes:
    if not data or len(data) % BLOCK_SIZE:
        raise ValueError("Padded plaintext must contain complete AES blocks")

    padding_length = data[-1]
    if (
        padding_length == 0
        or padding_length > BLOCK_SIZE
        or data[-padding_length:] != bytes([padding_length]) * padding_length
    ):
        raise ValueError("Invalid PKCS#7 padding")

    return data[:-padding_length]


def _make_padding_oracle(key: bytes) -> Callable[[bytes], bool]:
    def padding_oracle(iv_and_ciphertext: bytes) -> bool:
        if len(iv_and_ciphertext) < 2 * BLOCK_SIZE or len(iv_and_ciphertext) % BLOCK_SIZE:
            return False

        iv = iv_and_ciphertext[:BLOCK_SIZE]
        ciphertext = iv_and_ciphertext[BLOCK_SIZE:]
        decryptor = Cipher(algorithms.AES(key), modes.CBC(iv)).decryptor()
        padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        try:
            pkcs7_unpad(padded_plaintext)
        except ValueError:
            return False
        return True

    return padding_oracle


def create_challenge(plaintext: bytes) -> tuple[bytes, bytes, Callable[[bytes], bool]]:
    """Encrypt plaintext and return its IV, ciphertext, and key-isolated oracle."""
    key = secrets.token_bytes(32)
    iv = secrets.token_bytes(BLOCK_SIZE)
    encryptor = Cipher(algorithms.AES(key), modes.CBC(iv)).encryptor()
    ciphertext = encryptor.update(pkcs7_pad(plaintext)) + encryptor.finalize()
    return iv, ciphertext, _make_padding_oracle(key)
