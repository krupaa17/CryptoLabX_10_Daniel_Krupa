# CryptoLabX

**Course:** Cryptography Laboratory (22CPP307)
**Group:** 10
**SAST Tool:** Semgrep
**Application:** IoT Device Management

## About

CryptoLabX is a modular cryptography and security toolkit developed as part of the Cryptography Laboratory. The project is being developed progressively through laboratory assignments.

## Assignments

### Assignment 1 — CryptoLabX Toolkit

* Created the project structure and Git repository.
* Developed a menu-driven CLI.
* Implemented text-file analysis.
* Added character, word, line and letter-frequency analysis.
* Added execution logging.
* Added sample datasets.
* Documented the project.

### Assignment 2 — SAST

* Installed and configured **Semgrep**.
* Created an intentionally vulnerable Python program.
* Performed static security analysis.
* Generated a JSON Semgrep report.
* Documented SAST findings and terminal logs.

### Assignment 3 — IoT Device Management

Developed a small console-based IoT application with:

* Device registration
* Device status monitoring
* Firmware upload
* Device configuration

Intentionally introduced vulnerabilities:

* Command Injection
* Path Traversal
* Missing Authentication

The application was analyzed using Semgrep.

## Project Structure

```text
CryptoLabX/
├── classical/
├── modern/
├── hashing/
├── attacks/
├── analysis/
├── docs/
├── datasets/
├── outputs/
├── utils/
├── tests/
│
├── secure_application/
│   ├── src/
│   ├── reports/
│   ├── screenshots/
│   ├── sast/
│   ├── outputs/
│   ├── testcases/
│   ├── firmware/
│   └── README.md
│
├── main.py
├── README.md
└── requirements.txt
```

## Technologies

* Python
* Git & GitHub
* Semgrep
* Linux/WSL
* Command Line Interface

## Conclusion

CryptoLabX provides a foundation for learning cryptography, cryptanalysis, secure coding, and static security testing through practical laboratory assignments.
