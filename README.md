# CryptoLabX

CryptoLabX is a modular cryptanalysis toolkit being developed as part of the Cryptography Laboratory course. The project will gradually be extended throughout the semester with classical cryptography, cryptanalysis attacks, mathematical utilities, modern cryptography and statistical analysis modules.

### Week 1 

The objective of Week 1 is to establish the basic project structure and software foundation. No cryptographic algorithms are implemented in this version.

## Team Members

1. Krupa Joshi 
2. Daniel

## Project Structure

```text
CryptoLabX/
├── classical/      # Classical cryptography algorithms
├── attacks/        # Cryptanalysis and attack techniques
├── math/           # Mathematical utilities
├── modern/         # Modern cryptography modules
├── analysis/       # Statistical and frequency analysis
├── datasets/       # Input text files and datasets
├── outputs/        # Generated outputs
├── docs/           # Project documentation
├── tests/          # Testing files
├── utils/          # Utility functions
├── main.py         # Main command-line interface
├── README.md       # Project documentation
└── requirements.txt # Project dependencies
```

## Current Features

The Week 1 version provides:

* Menu-driven command-line interface
* Encrypt option
* Decrypt option
* Attack option
* Analyze option
* Exit option
* Text file analysis
* Character counting
* Unique character counting
* Letter frequency analysis
* Execution logging
* Dataset management

The Encrypt, Decrypt and Attack modules currently display "Coming Soon".

## File Analysis

The Analyze option reads a text file from the `datasets` folder and calculates:

* Number of characters
* Number of words
* Number of lines
* Number of unique characters
* Frequency of each alphabetic letter

## Logging

CryptoLabX maintains a log file named `crypto.log`.

The log records:

* Date
* Time
* Selected menu option

Example:

```text
2026-09-17 20:30:10 - Selected Option: Analyze
2026-09-17 20:31:05 - Selected Option: Exit
```

## Future Modules

Future versions of CryptoLabX will include:

### Classical Cryptography

* Caesar Cipher
* Monoalphabetic Substitution
* Vigenere Cipher
* Playfair Cipher
* Hill Cipher
* Transposition Ciphers

### Cryptanalysis Attacks

* Frequency Analysis
* Brute Force
* Known Plaintext Attacks
* Statistical Attacks

### Mathematical Utilities

* Modular Arithmetic
* GCD
* Extended Euclidean Algorithm
* Modular Inverse
* Prime Number Utilities

### Modern Cryptography

* Symmetric Encryption
* Public-Key Cryptography
* Hash Functions
* Digital Signatures

### Analysis

* Frequency Analysis
* Entropy
* Statistical Analysis

## Technologies

* Python
* Git
* GitHub
* Command Line Interface

## Version Control

The project uses Git for version control. Each team member should make meaningful commits during development.

## Conclusion

CryptoLabX provides the foundation for a reusable cryptanalysis toolkit. The Week 1 implementation focuses on project organization, command-line interaction, file handling, logging and documentation. Cryptographic algorithms will be added in future assignments.
