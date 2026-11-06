import random
import string

from .mt19937_stream_cipher import encrypt, decrypt


prefix_length = random.randint(5, 20)

prefix = ''.join(
    random.choice(string.ascii_letters + string.digits)
    for _ in range(prefix_length)
)

plaintext = (prefix + "A" * 14).encode()

actual_seed = random.randint(0, 65535)

ciphertext = encrypt(plaintext, actual_seed)

print("Original plaintext:", plaintext.decode())
print("Actual seed:", actual_seed)
print("Ciphertext:", ciphertext.hex())
print("Prefix length:", prefix_length)


known_text = b"A" * 14

matches = []

for candidate_seed in range(65536):
    decrypted = decrypt(ciphertext, candidate_seed)

    is_printable = all(32 <= b <= 126 for b in decrypted)

    if known_text in decrypted and is_printable:
        prefix_part = decrypted[:-14]

        if 5 <= len(prefix_part) <= 20:
            matches.append((candidate_seed, decrypted))


print("\nTotal seeds tested:", 65536)
print("Matching candidates:", len(matches))

if len(matches) == 1:
    recovered_seed, recovered_plaintext = matches[0]

    print("Recovered seed:", recovered_seed)
    print("Recovered plaintext:", recovered_plaintext.decode())
    print("Seed recovered:", recovered_seed == actual_seed)
    print("Known text found:", known_text in recovered_plaintext)
    print("Full plaintext verified:",
          decrypt(ciphertext, recovered_seed) == plaintext)
else:
    print("Unique seed recovery failed.")
