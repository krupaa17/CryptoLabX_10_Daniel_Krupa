from collections import Counter

from .shift_cipher import decrypt


ENGLISH_FREQUENCIES = {
    "A": 0.08167,
    "B": 0.01492,
    "C": 0.02782,
    "D": 0.04253,
    "E": 0.12702,
    "F": 0.02228,
    "G": 0.02015,
    "H": 0.06094,
    "I": 0.06966,
    "J": 0.00153,
    "K": 0.00772,
    "L": 0.04025,
    "M": 0.02406,
    "N": 0.06749,
    "O": 0.07507,
    "P": 0.01929,
    "Q": 0.00095,
    "R": 0.05987,
    "S": 0.06327,
    "T": 0.09056,
    "U": 0.02758,
    "V": 0.00978,
    "W": 0.02360,
    "X": 0.00150,
    "Y": 0.01974,
    "Z": 0.00074,
}


def chi_square_score(text):
    letters = [character.upper() for character in text if character.isalpha()]
    counts = Counter(letters)
    length = len(letters)
    if length == 0:
        return float("inf")
    return sum(
        (counts[letter] - length * expected) ** 2 / (length * expected)
        for letter, expected in ENGLISH_FREQUENCIES.items()
    )


def chi_square_attack(ciphertext):
    candidates = []
    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        candidates.append({"key": key, "plaintext": plaintext, "score": chi_square_score(plaintext)})
    return sorted(candidates, key=lambda item: (item["score"], item["key"]))


def best_chi_square_key(ciphertext):
    return chi_square_attack(ciphertext)[0]
