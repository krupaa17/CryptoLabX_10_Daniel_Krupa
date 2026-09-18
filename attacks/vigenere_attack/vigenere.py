from collections import Counter
from math import gcd
from string import ascii_uppercase


ALPHABET = ascii_uppercase
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


def clean_ciphertext(ciphertext):
    return "".join(character.upper() for character in ciphertext if character.isalpha())


def find_repeated_patterns(ciphertext, minimum_length=3, maximum_length=5):
    text = clean_ciphertext(ciphertext)
    patterns = {}
    for length in range(minimum_length, maximum_length + 1):
        for start in range(len(text) - length + 1):
            pattern = text[start:start + length]
            positions = [index for index in range(start + 1, len(text) - length + 1) if text[index:index + length] == pattern]
            if positions:
                patterns.setdefault(pattern, [start])
                patterns[pattern].extend(position for position in positions if position not in patterns[pattern])
    return {pattern: positions for pattern, positions in patterns.items() if len(positions) > 1}


def calculate_distances(repeated_patterns):
    distances = {}
    for pattern, positions in repeated_patterns.items():
        distances[pattern] = [right - left for left, right in zip(positions, positions[1:])]
    return distances


def find_factors(distance):
    if distance < 2:
        return []
    return [factor for factor in range(2, distance + 1) if distance % factor == 0]


def kasiski_analysis(ciphertext, maximum_key_length=20):
    repeated = find_repeated_patterns(ciphertext)
    distances = calculate_distances(repeated)
    scores = Counter()
    for pattern_distances in distances.values():
        for distance in pattern_distances:
            for factor in find_factors(distance):
                if factor <= maximum_key_length:
                    scores[factor] += 1
    return {
        "repeated_patterns": repeated,
        "distances": distances,
        "candidates": scores.most_common(),
    }


def calculate_ic(text):
    letters = clean_ciphertext(text)
    length = len(letters)
    if length < 2:
        return 0.0
    counts = Counter(letters)
    return sum(value * (value - 1) for value in counts.values()) / (length * (length - 1))


def split_into_groups(ciphertext, key_length):
    text = clean_ciphertext(ciphertext)
    return [text[index::key_length] for index in range(key_length)]


def frequency_analysis(group):
    letters = clean_ciphertext(group)
    counts = Counter(letters)
    length = len(letters)
    return {
        letter: {
            "count": counts[letter],
            "percentage": counts[letter] * 100 / length if length else 0.0,
        }
        for letter in ALPHABET
    }


def find_shift(group):
    letters = clean_ciphertext(group)
    length = len(letters)
    candidates = []
    for shift in range(26):
        decrypted = "".join(ALPHABET[(ALPHABET.index(letter) - shift) % 26] for letter in letters)
        counts = Counter(decrypted)
        score = sum(
            (counts[letter] - length * expected) ** 2 / (length * expected)
            for letter, expected in ENGLISH_FREQUENCIES.items()
        ) if length else float("inf")
        candidates.append((score, shift))
    return min(candidates)[1]


def find_key(groups):
    return "".join(ALPHABET[find_shift(group)] for group in groups)


def vigenere_decrypt(ciphertext, key):
    letters = clean_ciphertext(ciphertext)
    normalized_key = clean_ciphertext(key)
    if not normalized_key:
        raise ValueError("Key must contain at least one letter")
    return "".join(
        ALPHABET[(ALPHABET.index(letter) - ALPHABET.index(normalized_key[index % len(normalized_key)])) % 26]
        for index, letter in enumerate(letters)
    )


def vigenere_encrypt(plaintext, key):
    letters = clean_ciphertext(plaintext)
    normalized_key = clean_ciphertext(key)
    if not normalized_key:
        raise ValueError("Key must contain at least one letter")
    return "".join(
        ALPHABET[(ALPHABET.index(letter) + ALPHABET.index(normalized_key[index % len(normalized_key)])) % 26]
        for index, letter in enumerate(letters)
    )


def verify(plaintext, ciphertext, key):
    return vigenere_encrypt(plaintext, key) == clean_ciphertext(ciphertext)


def estimate_key_length(ciphertext, maximum_key_length=20):
    kasiski_candidates = kasiski_analysis(ciphertext, maximum_key_length)["candidates"]
    ic_scores = []
    for key_length in range(1, maximum_key_length + 1):
        groups = split_into_groups(ciphertext, key_length)
        average_ic = sum(calculate_ic(group) for group in groups) / len(groups)
        ic_scores.append((average_ic, key_length))
    ic_scores.sort(reverse=True)
    if kasiski_candidates:
        return kasiski_candidates[0][0]
    return ic_scores[0][1]
