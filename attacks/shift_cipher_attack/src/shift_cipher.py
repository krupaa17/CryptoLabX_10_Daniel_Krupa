def encrypt(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char

    return result


def decrypt(text, key):
    return encrypt(text, -key)


if __name__ == "__main__":
    message = "HELLO WORLD"
    key = 3

    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)

    print("Plaintext :", message)
    print("Key       :", key)
    print("Ciphertext:", encrypted)
    print("Decrypted  :", decrypted)

