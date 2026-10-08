from collections.abc import Callable

from .oracle import BLOCK_SIZE, pkcs7_unpad


def recover_plaintext(
    iv_and_ciphertext: bytes, padding_oracle: Callable[[bytes], bool]
) -> tuple[bytes, int]:
    """Recover plaintext and return the number of oracle queries made."""
    if len(iv_and_ciphertext) < 2 * BLOCK_SIZE or len(iv_and_ciphertext) % BLOCK_SIZE:
        raise ValueError("Input must contain an IV and at least one complete ciphertext block")

    blocks = [
        iv_and_ciphertext[offset : offset + BLOCK_SIZE]
        for offset in range(0, len(iv_and_ciphertext), BLOCK_SIZE)
    ]
    recovered = bytearray()
    query_count = 0

    for target_index in range(1, len(blocks)):
        original_previous = blocks[target_index - 1]
        target_block = blocks[target_index]
        intermediate = bytearray(BLOCK_SIZE)
        crafted_previous = bytearray(original_previous)
        target_prefix = b"".join(blocks[: target_index - 1])

        for position in range(BLOCK_SIZE - 1, -1, -1):
            padding_length = BLOCK_SIZE - position
            for suffix_position in range(position + 1, BLOCK_SIZE):
                crafted_previous[suffix_position] = intermediate[suffix_position] ^ padding_length

            found = False
            for intermediate_byte in range(256):
                crafted_previous[position] = intermediate_byte ^ padding_length
                query_count += 1
                if not padding_oracle(
                    target_prefix + bytes(crafted_previous) + target_block
                ):
                    continue

                if position > 0 and padding_length == 1:
                    confirmation = bytearray(crafted_previous)
                    confirmation[position - 1] ^= 1
                    query_count += 1
                    if not padding_oracle(
                        target_prefix + bytes(confirmation) + target_block
                    ):
                        continue

                intermediate[position] = intermediate_byte
                found = True
                break

            if not found:
                raise RuntimeError(
                    f"Padding oracle yielded no candidate for block {target_index}, "
                    f"byte {position}"
                )

        recovered.extend(
            intermediate_byte ^ previous_byte
            for intermediate_byte, previous_byte in zip(intermediate, original_previous)
        )

    return pkcs7_unpad(bytes(recovered)), query_count
