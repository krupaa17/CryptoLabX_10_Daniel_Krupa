# IoT Device Management System

## Lab Assignment 3 — Static Application Security Testing

**Course:** Cryptography Laboratory (22CPP307)
**Group:** 10
**Assigned Application:** IoT Device Management
**SAST Tool:** Semgrep
**Programming Language:** Python

---

## 1. Project Overview

This project implements a small console-based IoT Device Management System as part of Lab Assignment 3.

The purpose of the application is to demonstrate the core functionalities of an IoT device management system and perform Static Application Security Testing (SAST) using Semgrep.

The application is intentionally designed with selected security vulnerabilities for educational purposes. These vulnerabilities allow us to understand how insecure coding practices can affect an application and how SAST tools can be used to identify security issues.

This is a laboratory application and is not intended to be used as a production IoT management system.

---

## 2. Core Functionalities

The application provides the following four core functionalities:

### 1. Device Registration

Users can register a new IoT device by providing:

* Device ID
* Device name
* Device type

The registered device is stored in the application's runtime data structure.

### 2. Device Status Monitoring

The system displays information about registered devices, including:

* Device ID
* Device name
* Device type
* Current device status

### 3. Firmware Upload

The application allows the user to provide a firmware filename and attempts to read the corresponding firmware file from the firmware directory.

A dummy firmware file is used for laboratory demonstration.

### 4. Device Configuration

The application accepts a configuration command for a selected device and performs the requested configuration operation.

This functionality intentionally contains a command injection vulnerability for SAST demonstration.

---

## 3. Project Structure

```text
secure_application/
│
├── src/
│   └── iot_manager.py
│
├── reports/
│   └── findings.md
│
├── screenshots/
│
├── sast/
│   └── semgrep_report.json
│
├── outputs/
│
├── testcases/
│   └── testcases.txt
│
├── firmware/
│   └── update.bin
│
└── README.md
```

### Directory Description

| Directory/File | Purpose                                |
| -------------- | -------------------------------------- |
| `src/`         | Application source code                |
| `reports/`     | Security findings and analysis reports |
| `screenshots/` | Screenshots required for submission    |
| `sast/`        | Semgrep scan results                   |
| `outputs/`     | Generated application outputs          |
| `testcases/`   | Application test cases                 |
| `firmware/`    | Dummy firmware files used for testing  |
| `README.md`    | Project documentation                  |

---

## 4. Vulnerabilities

Three vulnerabilities were intentionally introduced into the application.

### 4.1 Command Injection

The device configuration functionality uses user-controlled input with `os.system()`.

```python
os.system(command)
```

This is insecure because user input is directly passed to the operating system shell.

**Potential impact:** An attacker could execute unintended operating-system commands.

---

### 4.2 Path Traversal

The firmware upload functionality constructs a file path using user-controlled input.

```python
filename = input("Enter firmware filename: ")
path = "firmware/" + filename
```

The filename is not properly validated before being used as a path.

**Potential impact:** An attacker could attempt to access files outside the intended firmware directory.

---

### 4.3 Missing Authentication

The application does not require authentication before allowing device configuration.

A user can directly select the configuration functionality from the main menu.

**Potential impact:** An unauthorized user could potentially modify device configuration.

---

## 5. SAST Tool — Semgrep

Semgrep is a Static Application Security Testing tool that analyzes source code for bugs, security vulnerabilities, and potentially dangerous coding patterns.

For this assignment, Semgrep was installed and used to analyze the Python application.

### Installation

The tool was installed using Python:

```bash
python3 -m pip install semgrep
```

The installation was verified using:

```bash
semgrep --version
```

The Semgrep version used during the experiment was:

```text
1.177.0
```

### Scan Command

The application was scanned using:

```bash
semgrep --config=auto secure_application/src/iot_manager.py
```

A JSON report was generated using:

```bash
semgrep --config=auto --json secure_application/src/iot_manager.py > secure_application/sast/semgrep_report.json
```

---

## 6. Semgrep Scan Result

The automatic Semgrep scan completed successfully.

The generated JSON report contained:

```text
"results": []
```

Therefore, the automatic ruleset did not report any findings for the tested source file.

The intentionally introduced vulnerabilities are documented in:

```text
reports/findings.md
```

No Semgrep Rule ID or severity has been assigned to vulnerabilities that were not reported by the actual scan.

This distinction is important because SAST results depend on the rules and analysis configuration used during scanning.

---

## 7. Test Cases

The following test cases were used to verify the application:

| Test Case | Description                      | Expected Result                                    |
| --------- | -------------------------------- | -------------------------------------------------- |
| TC01      | Register an IoT device           | Device is registered successfully                  |
| TC02      | View device status               | Device information is displayed                    |
| TC03      | Upload firmware                  | Firmware file is read successfully                 |
| TC04      | Configure device                 | Configuration operation is performed               |
| TC05      | Test command input               | Demonstrates command execution behavior            |
| TC06      | Test path input                  | Demonstrates insufficient path validation          |
| TC07      | Configure without authentication | Configuration is accessible without authentication |

---

## 8. Sample Execution

Run the application using:

```bash
python3 secure_application/src/iot_manager.py
```

The main menu is:

```text
==============================
     IoT Device Manager
==============================
1. Register Device
2. View Device Status
3. Upload Firmware
4. Configure Device
5. Exit
==============================
Enter your choice:
```

---

## 9. Logging and Documentation

The SAST laboratory work was performed in a logged terminal session using:

```bash
script sast_lab_log.txt
```

The terminal log records commands and their corresponding outputs during the experiment.

The project also contains the Semgrep machine-readable report:

```text
sast/semgrep_report.json
```

Security findings and analysis are documented in:

```text
reports/findings.md
```

---

## 10. Git Version Control

The project is maintained using Git and the same CryptoLabX repository created in the previous laboratory.

Example commits include:

```text
Create IoT application project structure
Implement IoT device management application
Add IoT application test cases
Run Semgrep analysis on IoT application
Document Semgrep findings and analysis
```

Git is used to track development, maintain the project history, and support collaboration among group members.

---

## 11. Learning Outcomes

Through this assignment, the following concepts were practiced:

* Development of a small security-focused application
* Identification of insecure coding practices
* Static Application Security Testing
* Semgrep installation and configuration
* Automated source-code analysis
* Security findings documentation
* Test-case development
* Git-based version control
* Security-focused code review

---

## 12. Conclusion

The IoT Device Management System was successfully developed as a small console-based Python application. It implements device registration, status monitoring, firmware handling, and configuration management.

Three vulnerabilities—Command Injection, Path Traversal, and Missing Authentication—were intentionally introduced for educational SAST testing.

Semgrep version 1.177.0 was used to perform the static analysis. The automatic Semgrep scan completed successfully but returned zero findings for the tested source file. The scan output and this result were documented without assigning unsupported rule IDs or severity values.

The assignment demonstrates the importance of secure coding practices, proper input validation, authentication, safe file handling, and the appropriate configuration of SAST tools.
