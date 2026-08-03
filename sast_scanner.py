import os
import re
import json
import argparse
from datetime import datetime

CUSTOM_RULES = [
    {
        "id": "SEC-001",
        "name": "SQL Injection (SQLi)",
        "severity": "High",
        "pattern": r"(SELECT|INSERT|UPDATE|DELETE).*\+.*['\"]|execute\(['\"].*%\s*\(",
        "recommendation": "Use parameterized queries or ORM to avoid SQL injection."
    },
    {
        "id": "SEC-002",
        "name": "Command Injection",
        "severity": "High",
        "pattern": r"os\.system\(|subprocess\.Popen\(|eval\(|exec\(",
        "recommendation": "Avoid using os.system or eval(). Use subprocess with shell=False."
    },
    {
        "id": "SEC-003",
        "name": "Hardcoded Credentials / API Keys",
        "severity": "High",
        "pattern": r"(?i)(api[_-]?key|password|secret|auth[_-]?token)\s*=\s*['\"][A-Za-z0-9_\-]{8,}['\"]",
        "recommendation": "Store secrets in environment variables or secret managers."
    },
    {
        "id": "SEC-004",
        "name": "Unsafe Deserialization / Dynamic Code",
        "severity": "Medium",
        "pattern": r"pickle\.loads\(|yaml\.load\(|eval\(",
        "recommendation": "Use safe_load for YAML or safer data structures like JSON."
    }
]

class DevSecOpsScanner:
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.results = []

    def scan_file_with_regex(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
                for line_num, line in enumerate(lines, start=1):
                    for rule in CUSTOM_RULES:
                        if re.search(rule["pattern"], line):
                            self.results.append({
                                "rule_id": rule["id"],
                                "issue": rule["name"],
                                "severity": rule["severity"],
                                "file": file_path,
                                "line": line_num,
                                "code": line.strip(),
                                "remediation": rule["recommendation"]
                            })
        except Exception as e:
            print(f"[-] Error reading {file_path}: {e}")

    def run_scan(self):
        print(f"[*] Starting SAST Scanner on directory: {self.target_dir}")
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                if file.endswith(".py") or file.endswith(".js"):
                    full_path = os.path.join(root, file)
                    self.scan_file_with_regex(full_path)
        print(f"[+] Scan completed! Found {len(self.results)} potential vulnerabilities.")

    def generate_html_report(self, output_filename="sast_report.html"):
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>SAST Vulnerability Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f4f6f9; }}
                h1 {{ color: #1a202c; }}
                .summary {{ margin-bottom: 20px; padding: 15px; background: #fff; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
                table {{ width: 100%; border-collapse: collapse; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
                th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #e2e8f0; }}
                th {{ background-color: #2d3748; color: white; }}
                .High {{ color: #e53e3e; font-weight: bold; }}
                .Medium {{ color: #dd6b20; font-weight: bold; }}
                code {{ background: #edf2f7; padding: 2px 6px; border-radius: 4px; }}
            </style>
        </head>
        <body>
            <h1>🛡️ Enterprise DevSecOps Code Auditor Report</h1>
            <div class="summary">
                <p><strong>Scan Date:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
                <p><strong>Target Directory:</strong> {self.target_dir}</p>
                <p><strong>Total Vulnerabilities Found:</strong> {len(self.results)}</p>
            </div>
            <table>
                <tr>
                    <th>Severity</th>
                    <th>Issue</th>
                    <th>File & Line</th>
                    <th>Vulnerable Code</th>
                    <th>Remediation</th>
                </tr>
        """
        for item in self.results:
            html_content += f"""
                <tr>
                    <td class="{item['severity']}">{item['severity']}</td>
                    <td>{item['issue']}</td>
                    <td>{os.path.basename(item['file'])} (Line {item['line']})</td>
                    <td><code>{item['code']}</code></td>
                    <td>{item['remediation']}</td>
                </tr>
            """
        html_content += """
            </table>
        </body>
        </html>
        """
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[+] HTML Report generated successfully: {output_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enterprise DevSecOps SAST Scanner")
    parser.add_argument("-d", "--dir", default=".", help="Directory to scan")
    parser.add_argument("-o", "--output", default="sast_report.html", help="HTML Output file name")
    args = parser.parse_args()

    scanner = DevSecOpsScanner(args.dir)
    scanner.run_scan()
    scanner.generate_html_report(args.output)
