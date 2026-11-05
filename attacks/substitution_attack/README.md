# Assignment 6: Monoalphabetic Substitution Cryptanalysis

## Required Functions

- `frequency_analysis()` counts ciphertext letters and calculates percentages.
- `word_frequency_analysis()` ranks repeated words.
- `pattern_analysis()` groups words by repeated-letter patterns.
- `apply_substitution()` applies a proposed mapping.
- `display_partial_plaintext()` displays the current hypothesis.
- `verify_solution()` re-encrypts plaintext and checks the ciphertext.

The implementation also provides `encrypt_substitution()` and `decrypt_substitution()` for generating and checking ciphertext.

## Run

```text
python -m attacks.substitution_attack.main attacks/substitution_attack/testcases/sample_plaintext.txt
```

The sample is an original educational fixture. A permitted one-page excerpt from the assigned textbook can be supplied as an input file for the laboratory experiment.

## Analysis Record

The experiment should record the most frequent letters, one-, two-, and three-letter words, repeated words, repeated-letter patterns, each candidate substitution, the resulting partial plaintext, and the decision to keep or reject the hypothesis.
