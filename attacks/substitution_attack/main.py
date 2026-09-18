import argparse
from pathlib import Path

from .substitution import (
    decrypt_substitution,
    display_partial_plaintext,
    encrypt_substitution,
    frequency_analysis,
    pattern_analysis,
    verify_solution,
    word_frequency_analysis,
)


def analyze_ciphertext(ciphertext):
    return {
        "frequency": frequency_analysis(ciphertext),
        "word_frequency": word_frequency_analysis(ciphertext),
        "patterns": pattern_analysis(ciphertext),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ciphertext", type=Path)
    arguments = parser.parse_args()
    ciphertext = arguments.ciphertext.read_text(encoding="utf-8")
    analysis = analyze_ciphertext(ciphertext)
    print("Frequency:", analysis["frequency"])
    print("Words:", analysis["word_frequency"])
    print("Patterns:", analysis["patterns"])
    print("Partial plaintext:", display_partial_plaintext(ciphertext, {}))


if __name__ == "__main__":
    main()
