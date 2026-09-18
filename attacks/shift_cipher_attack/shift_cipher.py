from string import ascii_uppercase


ALPHABET = ascii_uppercase


def encrypt(plaintext, key):
    return _transform(plaintext, key)


def decrypt(ciphertext, key):
    return _transform(ciphertext, -key)


def _transform(text, shift):
    result = []
    for character in text:
        if character.isalpha():
            alphabet = ascii_uppercase if character.isupper() else ascii_uppercase.lower()
            result.append(alphabet[(alphabet.index(character) + shift) % 26])
        else:
            result.append(character)
    return "".join(result)
