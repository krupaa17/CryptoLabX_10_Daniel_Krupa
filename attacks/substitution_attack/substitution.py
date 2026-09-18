from collections import Counter
from string import ascii_uppercase


ALPHABET = ascii_uppercase


def apply_substitution(text, mapping):
    return "".join(mapping.get(character.upper(), character) for character in text)


def encrypt_substitution(plaintext, key):
    normalized_key = {letter.upper(): value.upper() for letter, value in key.items()}
    return apply_substitution(plaintext, normalized_key)


def decrypt_substitution(ciphertext, key):
    normalized_key = {value.upper(): letter.upper() for letter, value in key.items()}
    return apply_substitution(ciphertext, normalized_key)


def frequency_analysis(ciphertext):
    letters = [character for character in ciphertext.upper() if character in ALPHABET]
    counts = Counter(letters)
    total = len(letters)
    return [
        {
            "letter": letter,
            "count": counts[letter],
            "percentage": counts[letter] * 100 / total if total else 0.0,
        }
        for letter in sorted(ALPHABET, key=lambda item: (-counts[item], item))
    ]


def word_frequency_analysis(ciphertext):
    words = [word for word in "".join(character if character.isalpha() else " " for character in ciphertext.upper()).split()]
    counts = Counter(words)
    return counts.most_common()


def pattern_signature(word):
    labels = {}
    next_label = 0
    signature = []
    for letter in word.upper():
        if letter not in labels:
            labels[letter] = next_label
            next_label += 1
        signature.append(labels[letter])
    return tuple(signature)


def pattern_analysis(ciphertext):
    words = [word for word in "".join(character if character.isalpha() else " " for character in ciphertext.upper()).split()]
    patterns = {}
    for word in words:
        patterns.setdefault(pattern_signature(word), []).append(word)
    return patterns


def display_partial_plaintext(ciphertext, substitutions):
    return apply_substitution(ciphertext, {key.upper(): value.upper() for key, value in substitutions.items()})


def verify_solution(plaintext, ciphertext, key):
    return encrypt_substitution(plaintext, key) == ciphertext.upper()
