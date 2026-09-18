from .vigenere import (
    calculate_ic,
    find_key,
    frequency_analysis,
    kasiski_analysis,
    split_into_groups,
    vigenere_decrypt,
    verify,
)


def analyze(ciphertext, key_length=None):
    analysis = kasiski_analysis(ciphertext)
    selected_length = key_length or (analysis["candidates"][0][0] if analysis["candidates"] else 1)
    groups = split_into_groups(ciphertext, selected_length)
    key = find_key(groups)
    plaintext = vigenere_decrypt(ciphertext, key)
    return {
        "estimated_key_length": selected_length,
        "kasiski": analysis,
        "groups": groups,
        "frequency_tables": [frequency_analysis(group) for group in groups],
        "index_of_coincidence": [calculate_ic(group) for group in groups],
        "key": key,
        "plaintext": plaintext,
        "verified": verify(plaintext, ciphertext, key),
    }


def main():
    ciphertext = input("Enter ciphertext: ")
    result = analyze(ciphertext)
    print("Estimated key length:", result["estimated_key_length"])
    print("Recovered key:", result["key"])
    print("Recovered plaintext:", result["plaintext"])
    print("Verification:", result["verified"])


if __name__ == "__main__":
    main()
