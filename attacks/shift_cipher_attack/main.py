from .brute_force_dictionary import best_dictionary_key
from .chi_square_attack import best_chi_square_key
from .shift_cipher import decrypt, encrypt


def compare_attacks(ciphertext, dictionary=None):
    dictionary_result = best_dictionary_key(ciphertext, dictionary)
    chi_square_result = best_chi_square_key(ciphertext)
    return {
        "dictionary": dictionary_result,
        "chi_square": chi_square_result,
    }


def main():
    plaintext = input("Enter plaintext or ciphertext: ")
    mode = input("Enter mode (encrypt, decrypt, attack): ").strip().lower()
    if mode in {"encrypt", "decrypt"}:
        key = int(input("Enter shift key (0-25): "))
        result = encrypt(plaintext, key) if mode == "encrypt" else decrypt(plaintext, key)
        print(result)
        return
    if mode == "attack":
        results = compare_attacks(plaintext)
        print("Dictionary key:", results["dictionary"]["key"])
        print("Dictionary plaintext:", results["dictionary"]["plaintext"])
        print("Chi-square key:", results["chi_square"]["key"])
        print("Chi-square plaintext:", results["chi_square"]["plaintext"])
        return
    print("Invalid mode.")


if __name__ == "__main__":
    main()
