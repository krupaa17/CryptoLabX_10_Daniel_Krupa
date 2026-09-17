import os
import re
from collections import Counter


def analyze_file(filename):
    filepath = os.path.join("datasets", filename)

    if not os.path.exists(filepath):
        print("File not found.")
        return

    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()

    characters = len(text)
    words = len(re.findall(r"\b\w+\b", text))
    lines = len(text.splitlines())
    unique_characters = len(set(text))

    letters = [char.lower() for char in text if char.isalpha()]
    frequency = Counter(letters)

    print("\n----- File Analysis -----")
    print("File:", filename)
    print("Number of characters:", characters)
    print("Number of words:", words)
    print("Number of lines:", lines)
    print("Unique characters:", unique_characters)

    print("\nLetter Frequency:")

    for letter in sorted(frequency):
        print(f"{letter} : {frequency[letter]}")


def menu():
    while True:
        print("\n==========================")
        print("        CryptoLabX")
        print("==========================")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Attack")
        print("4. Analyze")
        print("5. Exit")
        print("==========================")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Encryption module: Coming Soon")

        elif choice == "2":
            print("Decryption module: Coming Soon")

        elif choice == "3":
            print("Attack module: Coming Soon")

        elif choice == "4":
            filename = input("Enter dataset filename: ")
            analyze_file(filename)

        elif choice == "5":
            print("Exiting CryptoLabX...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()