# Assignment 5: Vigenere Cryptanalysis

## Required Workflow

1. `clean_ciphertext()` normalizes the input.
2. `find_repeated_patterns()` and `calculate_distances()` support Kasiski examination.
3. `find_factors()` and `kasiski_analysis()` estimate candidate key lengths.
4. `calculate_ic()` provides Index of Coincidence values.
5. `split_into_groups()` separates positions for frequency analysis.
6. `frequency_analysis()` creates A-Z frequency tables.
7. `find_shift()` and `find_key()` recover a probable key.
8. `vigenere_decrypt()` recovers plaintext.
9. `vigenere_encrypt()` and `verify()` validate the result.

## Run

```text
python -m attacks.vigenere_attack.main
```

The supplied even-group ciphertext is in `testcases/even_group_ciphertext.txt`.

## Failure Analysis

Kasiski examination is less reliable when repeated patterns are rare or when the ciphertext is short. Frequency analysis also becomes noisy for short groups. Candidate key lengths should be compared with Index of Coincidence values and the recovered plaintext should be verified by re-encryption.
