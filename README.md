# 🛡️ Enterprise DevSecOps Code Auditor & Vulnerability Scanner (SAST Engine)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Security: SAST](https://img.shields.io/badge/Security-SAST%20Auditor-red.svg)](https://owasp.org/)
[![DevSecOps Integrated](https://img.shields.io/badge/DevSecOps-Automated-green.svg)]()

## 📌 Executive Summary
**Enterprise DevSecOps Code Auditor** is a custom Static Application Security Testing (SAST) tool built to automate source code security auditing within modern Continuous Integration and Continuous Deployment (CI/CD) pipelines. 

Instead of relying solely on manual security reviews, this tool proactively scans source code files for critical **OWASP Top 10** vulnerabilities, hardcoded secrets, dangerous function calls, and insecure deserialization flaws before code reaches production environments.

---

## 🛠️ Key Technical Features

### 1. 🔍 Static Analysis & Pattern Detection
- **Custom Hybrid Regex Engine:** High-performance detection pattern targeting common code flaws in Python and JavaScript applications.
- **OWASP Top 10 Flaw Detection:**
  - **SQL Injection (SQLi):** Identifies dynamic string concatenations inside database query executions.
  - **Command Injection:** Detects unsafe usage of OS command executions like `os.system()` and `subprocess.Popen()`.
  - **Hardcoded Credentials & Secrets:** Scans for embedded API keys, JWT tokens, AWS keys, and hardcoded passwords.
  - **Unsafe Deserialization & Dynamic Code Execution:** Pinpoints vulnerable dynamic code functions such as `eval()`, `exec()`, and `pickle.loads()`.

### 2. 📊 Interactive Audit Reporting
- **Automated HTML Report Generation:** Converts raw vulnerability findings into a clean, interactive, and visually structured HTML document.
- **Severity Classification:** Automatically categorizes findings into **High**, **Medium**, and **Low** risk levels.
- **Actionable Remediation Guidance:** Provides precise code location (File + Line Number) and concrete recommendations for developers to patch detected flaws.

---

## 🏗️ Project Architecture & Workflow

```text
  [ Source Code / Repository ]
               │
               ▼
  [ SAST Scanner Engine (Regex & AST Parsing) ]
               │
               ├──────► Check for Hardcoded Secrets
               ├──────► Check for SQL & Command Injections
               └──────► Check for Dangerous Functions (eval/pickle)
               │
               ▼
  [ Vulnerability Assessment & Risk Scoring ]
               │
               ▼
  [ Output: Interactive HTML Security Audit Report ]


🚀 Installation & Usage Guide
Prerequisites
Python 3.8+ installed on your system.
Standard Python libraries (os, re, json, argparse, datetime).


1. Clone the Repository
      git clone [https://github.com/Omar-Sherif2026/CodeAlpha_Enterprise_SAST_Scanner.git](https://github.com/Omar-Sherif2026/CodeAlpha_Enterprise_SAST_Scanner.git)
cd CodeAlpha_Enterprise_SAST_Scanner


2. Run the SAST Scanner
Execute the scanner against any project directory (or the included test application):
    python sast_scanner.py -d . -o sast_report.html


3. Command Line Arguments
-d, --dir: Target directory to audit (Default: current directory .).
-o, --output: Output file name for the generated report (Default: sast_report.html).

<img width="1910" height="1019" alt="لقطة شاشة 2026-08-04 004714" src="https://github.com/user-attachments/assets/b4088cd4-75b0-46f1-ab9e-cf2aaa358f92" />

<img width="1911" height="869" alt="لقطة شاشة 2026-08-04 004134" src="https://github.com/user-attachments/assets/8292b71e-8d91-4d48-bbf8-4d80e0c4a0f5" />

<img width="1911" height="869" alt="لقطة شاشة 2026-08-04 004134" src="https://github.com/user-attachments/assets/b07bc86e-506e-44dd-a509-3aa77fb5dbee" />

<img width="1911" height="869" alt="لقطة شاشة 2026-08-04 004134" src="https://github.com/user-attachments/assets/e4173cc9-2790-4930-ac26-5555ce67a564" />

🛡️ Remediation Strategy & DevSecOps Best Practices
Never Hardcode Secrets: Use environment variables or Secret Management solutions (e.g., HashiCorp Vault, AWS Secrets Manager).
Parameterized Queries: Enforce the use of Prepared Statements or Object-Relational Mapping (ORM) frameworks to mitigate SQL Injection risks.
Input Sanitization: Avoid executing arbitrary shell commands from user input; use strict input validation and safe APIs.


👤 Author & Contact Information
Name: Omar Sherif
Domain: Cyber Security Intern
Company: CodeAlpha
Role Target: DevSecOps / Application Security / Penetration Tester
GitHub: Omar-Sherif2026
LinkedIn: Omar Sherif
