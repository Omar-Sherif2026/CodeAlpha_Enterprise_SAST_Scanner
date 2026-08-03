# 🛡️ Enterprise DevSecOps Code Auditor & Vulnerability Scanner (SAST)

An automated Static Application Security Testing (SAST) tool built in Python to scan source code for OWASP Top 10 vulnerabilities, hardcoded secrets, and unsafe function execution within DevSecOps environments.

## 🚀 Key Features
- **OWASP Top 10 Coverage:** Detects SQL Injection (SQLi), Command Injection, and Unsafe Deserialization (`eval`, `pickle`).
- **Secret Detection:** Scans for hardcoded API keys, secrets, and auth tokens via custom Regex patterns.
- **Interactive Reporting:** Generates a structured **HTML Audit Report** with issue severity and recommended remediations.

## 🛠️ Installation & Usage

```bash
# Clone the repository
git clone [https://github.com/Omar-Sherif2026/CodeAlpha_Enterprise_SAST_Scanner.git](https://github.com/Omar-Sherif2026/CodeAlpha_Enterprise_SAST_Scanner.git)

# Run the SAST Scanner
python sast_scanner.py -d . -o sast_report.html
