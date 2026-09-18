from shift_cipher import encrypt, decrypt
from brute_force_dictionary import attack as dictionary_attack
from chi_square_attack import attack as chi_square_attack


def main():
    print("===================================")
    print("      Shift Cipher Cryptanalysis")
    print("===================================")

    plaintext = input("Enter plaintext: ")
    key = int(input("Enter key (0-25): "))

    ciphertext = encrypt(plaintext, key)

    print("\nCiphertext:", ciphertext)

    print("\n--- Dictionary Attack ---")

    dictionary_results = dictionary_attack(ciphertext)
    best_dictionary = dictionary_results[0]

    print("Predicted Key:", best_dictionary[1])
    print("Plaintext:", best_dictionary[2])
    print("Dictionary Score:", best_dictionary[0])

    print("\n--- Chi-Square Attack ---")

    chi_results = chi_square_attack(ciphertext)
    best_chi = chi_results[0]

    print("Predicted Key:", best_chi[1])
    print("Plaintext:", best_chi[2])
    print("Chi-Square Score:", round(best_chi[0], 2))

    print("\n--- Comparison ---")
    print("Actual Key:", key)
    print("Dictionary Key:", best_dictionary[1])
    print("Chi-Square Key:", best_chi[1])

    print(
        "Dictionary Correct:",
        best_dictionary[1] == key
    )

    print(
        "Chi-Square Correct:",
        best_chi[1] == key
    )


if __name__ == "__main__":
    main()
