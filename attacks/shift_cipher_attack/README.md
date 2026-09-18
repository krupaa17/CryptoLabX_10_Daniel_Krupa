# Assignment 4: Shift Cipher Cryptanalysis

## Contents

- `shift_cipher.py` implements Shift Cipher encryption and decryption.
- `brute_force_dictionary.py` tests all keys and ranks plaintext using an English dictionary.
- `chi_square_attack.py` tests all keys and ranks plaintext using English letter frequencies.
- `main.py` compares dictionary scoring and chi-square analysis.

## Run

```text
python -m attacks.shift_cipher_attack.main
```

## Required Comparison

The CLI reports the key predicted by dictionary scoring and the key predicted by chi-square analysis. The results should be compared with the actual key for each test case.

## Failure Analysis

Dictionary scoring can fail when the plaintext is short, contains uncommon words, or uses a dictionary that does not contain the vocabulary. Chi-square analysis can fail on short texts because letter frequencies are not representative. Longer ciphertext, a larger dictionary, and combined scoring improve reliability.
