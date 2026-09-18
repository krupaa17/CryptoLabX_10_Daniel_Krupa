from shift_cipher import decrypt


def load_dictionary():
    words = set()

    with open(
        "../dictionary/english_words.txt",
        "r",
        encoding="utf-8"
    ) as file:
        for word in file:
            words.add(word.strip().lower())

    return words


def dictionary_score(text, dictionary):
    words = text.lower().split()
    score = 0

    for word in words:
        word = ''.join(char for char in word if char.isalpha())

        if word in dictionary:
            score += 1

    return score


def attack(ciphertext):
    dictionary = load_dictionary()

    candidates = []

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = dictionary_score(plaintext, dictionary)

        candidates.append((score, key, plaintext))

    candidates.sort(reverse=True)

    return candidates


if __name__ == "__main__":
    ciphertext = input("Enter ciphertext: ")

    results = attack(ciphertext)

    print("\nDictionary Attack Results:")

    for score, key, plaintext in results:
        print(
            f"Key: {key:2} | Score: {score:2} | "
            f"Plaintext: {plaintext}"
        )

    best = results[0]

    print("\nPredicted Key:", best[1])
    print("Predicted Plaintext:", best[2])
