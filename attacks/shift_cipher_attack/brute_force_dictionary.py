from pathlib import Path

from .shift_cipher import decrypt


DEFAULT_DICTIONARY = Path(__file__).parent / "dictionary" / "english_words.txt"


def load_dictionary(path=DEFAULT_DICTIONARY):
    return {
        word.strip().lower()
        for word in Path(path).read_text(encoding="utf-8").splitlines()
        if word.strip()
    }


def dictionary_score(text, words):
    tokens = [token.lower() for token in text.split()]
    return sum(token.strip(".,!?;:'\"()[]{}").isalpha() and token.strip(".,!?;:'\"()[]{}").lower() in words for token in tokens)


def brute_force_dictionary(ciphertext, dictionary=None):
    words = load_dictionary() if dictionary is None else set(dictionary)
    candidates = []
    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = dictionary_score(plaintext, words)
        candidates.append({"key": key, "plaintext": plaintext, "score": score})
    return sorted(candidates, key=lambda item: (-item["score"], item["key"]))


def best_dictionary_key(ciphertext, dictionary=None):
    return brute_force_dictionary(ciphertext, dictionary)[0]
