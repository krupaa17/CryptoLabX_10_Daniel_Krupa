from shift_cipher import decrypt


ENGLISH_FREQUENCY = {
    'a': 8.167,
    'b': 1.492,
    'c': 2.782,
    'd': 4.253,
    'e': 12.702,
    'f': 2.228,
    'g': 2.015,
    'h': 6.094,
    'i': 6.966,
    'j': 0.153,
    'k': 0.772,
    'l': 4.025,
    'm': 2.406,
    'n': 6.749,
    'o': 7.507,
    'p': 1.929,
    'q': 0.095,
    'r': 5.987,
    's': 6.327,
    't': 9.056,
    'u': 2.758,
    'v': 0.978,
    'w': 2.360,
    'x': 0.150,
    'y': 1.974,
    'z': 0.074
}


def chi_square_score(text):
    letters = [
        char.lower()
        for char in text
        if char.isalpha()
    ]

    total = len(letters)

    if total == 0:
        return float("inf")

    score = 0

    for letter in ENGLISH_FREQUENCY:
        observed = letters.count(letter)
        expected = total * ENGLISH_FREQUENCY[letter] / 100

        score += ((observed - expected) ** 2) / expected

    return score


def attack(ciphertext):
    results = []

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = chi_square_score(plaintext)

        results.append((score, key, plaintext))

    results.sort()

    return results


if __name__ == "__main__":
    ciphertext = input("Enter ciphertext: ")

    results = attack(ciphertext)

    print("\nChi-Square Attack Results:")

    for score, key, plaintext in results:
        print(
            f"Key: {key:2} | "
            f"Chi-Square: {score:.2f} | "
            f"Plaintext: {plaintext}"
        )

    best = results[0]

    print("\nPredicted Key:", best[1])
    print("Predicted Plaintext:", best[2])
