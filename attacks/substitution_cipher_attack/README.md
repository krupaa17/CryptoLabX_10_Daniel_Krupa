# Assignment 5 - Monoalphabetic Substitution Cipher Cryptanalysis

## Objective

The objective of this assignment is to implement a monoalphabetic substitution cipher and perform cryptanalysis using:

* Letter-frequency analysis
* Word-frequency analysis
* Word-pattern analysis
* Repeated words
* Iterative substitution testing
* Plaintext recovery
* Key verification

Python is not used for this assignment. The implementation is written in C++.

## Group Information

Group Number: 10

Assigned page:

$$
10 + 30 = 40
$$

The plaintext used for the experiment is taken from page 40 of *Modern Cryptography* by Katz and Lindell.

## Folder Structure

```text
substitution_cipher_attack/
├── src/
│   ├── substitution_cipher.cpp
│   └── main.cpp
├── testcases/
│   ├── plaintext.txt
│   └── ciphertext.txt
├── outputs/
├── screenshots/
├── reports/
└── README.md
```

## Monoalphabetic Substitution Cipher

A monoalphabetic substitution cipher replaces every plaintext letter with a fixed ciphertext letter.

The same substitution is used throughout the entire message.

For example:

```text
Plain :  A B C D E ...
Cipher:  Q W E R T ...
```

## Cryptanalysis

### 1. Frequency Analysis

The frequency of every ciphertext letter is counted and displayed in descending order. Percentage frequencies are also calculated.

The frequency distribution is compared with typical English letter frequencies to generate possible substitutions.

### 2. Word Frequency Analysis

Ciphertext words are extracted and counted.

Special attention is given to:

* One-letter words
* Two-letter words
* Three-letter words
* Repeated words

These provide clues about possible plaintext words.

### 3. Pattern Analysis

Each word is converted into a repeated-letter pattern.

For example:

```text
MEET → 0112
```

Words with identical patterns can represent possible substitution candidates.

### 4. Iterative Recovery

Candidate substitutions are tested one at a time.

The partial plaintext is displayed after each substitution.

If a hypothesis produces meaningful text, it is retained. If it produces inconsistent or meaningless text, it is rejected and another hypothesis is tested.

### 5. Verification

After recovering the plaintext and substitution key, the plaintext is encrypted again using the recovered key.

The generated ciphertext is compared with the original ciphertext.

If both are identical, the recovered solution is verified.

## Required Functions

The program contains the following required functions:

```text
frequency_analysis()
word_frequency_analysis()
pattern_analysis()
apply_substitution()
display_partial_plaintext()
verify_solution()
```

Additional functions are used for key display and interactive cryptanalysis.

## Compilation

From the `src` directory:

```bash
g++ substitution_cipher.cpp -o substitution_cipher
g++ main.cpp -o substitution_attack
```

## Execution

Generate ciphertext:

```bash
./substitution_cipher
```

Run cryptanalysis:

```bash
./substitution_attack
```

## Results

The experimental results, recovered substitutions, partial plaintext observations, and final verification are documented in the notebook.

## Conclusion

The monoalphabetic substitution cipher was implemented successfully and its ciphertext was analyzed using frequency, word-frequency, and pattern analysis.

The cryptanalysis was performed iteratively by proposing substitutions, examining partial plaintext, rejecting incorrect hypotheses, and retaining substitutions that produced meaningful English text.

The recovered substitution key was then validated by re-encrypting the recovered plaintext and comparing the generated ciphertext with the original ciphertext.
