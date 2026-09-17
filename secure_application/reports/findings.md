# SAST Findings Report

### Application: IoT Device Management
### Group: 10
### SAST Tool: Semgrep
### Semgrep Version: 1.177.0
---

## 1. Application Overview

The IoT Device Management application is a small console-based Python application developed for demonstrating basic IoT device management functionalities.

The application provides the following core functionalities:

1. Smart device registration
2. Device status monitoring
3. Firmware upload
4. Device configuration management

The application was intentionally designed with selected insecure coding practices for educational SAST analysis.

---

## 2. Vulnerabilities Intentionally Introduced

Three vulnerabilities were intentionally included in the application.

| No. | Vulnerability          | Location             | Description                                                           | Expected Security Impact                                               |
| --- | ---------------------- | -------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 1   | Command Injection      | `configure_device()` | User-provided configuration input is passed directly to `os.system()` | An attacker may execute unintended operating-system commands           |
| 2   | Path Traversal         | `upload_firmware()`  | User-controlled filename is directly combined with the firmware path  | An attacker may attempt to access files outside the intended directory |
| 3   | Missing Authentication | `configure_device()` | Device configuration can be accessed without authentication           | An unauthorized user may modify device configuration                   |

---

## 3. Semgrep Scan

The application was scanned using Semgrep with the following command:

```bash
semgrep --config=auto secure_application/src/iot_manager.py
```

A machine-readable JSON report was generated using:

```bash
semgrep --config=auto --json secure_application/src/iot_manager.py > secure_application/sast/semgrep_report.json
```

### Scan Result

Semgrep version `1.177.0` was used for the analysis.

The generated JSON report contained:

```text
"results": []
```

Therefore, the automatic Semgrep scan did not report any findings for this particular source file using the selected automatic ruleset.

---

## 4. Findings Table

| No. | Vulnerability          | Semgrep Rule ID | Semgrep Severity | Semgrep Result                 |
| --- | ---------------------- | --------------- | ---------------- | ------------------------------ |
| 1   | Command Injection      | Not reported    | Not reported     | Not detected by automatic scan |
| 2   | Path Traversal         | Not reported    | Not reported     | Not detected by automatic scan |
| 3   | Missing Authentication | Not reported    | Not reported     | Not detected by automatic scan |

The vulnerabilities listed above were intentionally included in the application, but they were not reported by the `--config=auto` Semgrep scan. Therefore, no Semgrep Rule ID or severity has been assigned to these findings.

---

## 5. Analysis

The Semgrep scan completed successfully without reporting errors. However, the automatic ruleset produced zero findings for the test program.

This demonstrates that a successful SAST scan does not necessarily mean that source code contains no security weaknesses. SAST tools depend on the rules and analysis techniques being applied. Custom rules or additional security rules may be required to identify specific application-level vulnerabilities.

The intentionally vulnerable code was retained for educational purposes so that the vulnerabilities can be discussed and manually reviewed.

---

## 6. Conclusion

The IoT Device Management application was successfully developed and analyzed using Semgrep. The application contains three intentionally introduced vulnerabilities: Command Injection, Path Traversal, and Missing Authentication.

Semgrep version 1.177.0 completed the automatic scan successfully, but the selected automatic ruleset reported zero findings for the application. The result was documented rather than incorrectly assigning Rule IDs or severity levels that were not produced by the tool.

This exercise demonstrates the importance of understanding both the vulnerabilities present in source code and the rules used by a SAST tool during security analysis.
