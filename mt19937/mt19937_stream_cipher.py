import numpy as np

def generate_keystream(seed, length):
    bit_generator = np.random.MT19937(seed)
    rng = np.random.Generator(bit_generator)

    return rng.integers(
        0, 256,
        size=length,
        dtype=np.uint8
    )


def encrypt_decrypt(data, seed):
    keystream = generate_keystream(seed, len(data))

    result = bytearray()

    for i in range(len(data)):
        result.append(data[i] ^ int(keystream[i]))

    return bytes(result)


def encrypt(plaintext, seed):
    return encrypt_decrypt(plaintext, seed)


def decrypt(ciphertext, seed):
    return encrypt_decrypt(ciphertext, seed)


if __name__ == "__main__":
    message = b"HELLO CRYPTOGRAPHY"
    seed = 12345

    ciphertext = encrypt(message, seed)
    decrypted = decrypt(ciphertext, seed)

    print("Plaintext:", message)
    print("Ciphertext:", ciphertext.hex())
    print("Decrypted:", decrypted)
    print("Encryption successful:", ciphertext != message)
    print("Decryption successful:", decrypted == message)
