import argparse
from pathlib import Path

from .oracle import create_challenge
from .padding_oracle import recover_plaintext


DEFAULT_PLAINTEXT = (
    b"Padding oracles reveal plaintext one byte at a time without the AES key."
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Demonstrate recovery of AES-CBC plaintext using a padding oracle."
    )
    parser.add_argument(
        "--input",
        type=Path,
        help="read the challenge plaintext from a file instead of using the built-in sample",
    )
    arguments = parser.parse_args()
    plaintext = arguments.input.read_bytes() if arguments.input else DEFAULT_PLAINTEXT

    iv, ciphertext, padding_oracle = create_challenge(plaintext)
    recovered, query_count = recover_plaintext(iv + ciphertext, padding_oracle)

    print(f"IV: {iv.hex()}")
    print(f"Ciphertext: {ciphertext.hex()}")
    print(f"Recovered plaintext ({len(recovered)} bytes): {recovered!r}")
    print(f"Oracle queries: {query_count}")


if __name__ == "__main__":
    main()
