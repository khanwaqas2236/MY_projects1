# SWAT - Security Web Assessment Tool

![SWAT Banner](https://img.shields.io/badge/SWAT-Web%20Security%20Tool-red)
![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20Mac-orange)

A powerful Metasploit-style web vulnerability scanner with interactive exploitation demonstrations and visible proof-of-concept attacks.

## 🚀 Features

- **Metasploit-style Interface**: Professional command-line interface with colored output
- **Multiple Scan Modules**: Subdomain enumeration, XSS, SQL injection, redirect checks
- **Visible Exploitation**: Generate interactive HTML demos showing actual attack proofs
- **Educational Tool**: Perfect for learning web application security
- **Cross-Platform**: Works on Linux, Windows, and macOS

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

git clone https://github.com/YOUR_USERNAME/my-projects.git
cd my-projects/swat-scanner

## Step 2: Install Dependencies
bash
pip install colorama
Step 3: Run the Tool
bash
python swat_scanner.py

# Start the tool
python swat_scanner.py

# Show available modules
swat> show modules

# Use a specific module
swat> use xss_scanner

# Set target
swat(xss_scanner)> set TARGET testfire.net

# Run the scan
swat(xss_scanner)> run
Available Modules
subdomain_enum - Discover subdomains

xss_scanner - Cross-Site Scripting detection

sqli_detector - SQL Injection vulnerability scanning

redirect_check - Open redirect vulnerability checks

full_audit - Comprehensive web application audit

## 🛠️ Usage Examples
Example 1: Full Website Audit
bash
swat> use full_audit
swat(full_audit)> set TARGET example.com
swat(full_audit)> run

## Example 2: SQL Injection Testing
swat> use sqli_detector
swat(sqli_detector)> set TARGET testphp.vulnweb.com
swat(sqli_detector)> run
Example 3: Subdomain Discovery
bash
swat> use subdomain_enum
swat(subdomain_enum)> set TARGET google.com
swat(subdomain_enum)> run

## 🎪 Exploitation Demos
After scanning, SWAT can generate interactive HTML demonstrations:

## XSS Demo
Creates an HTML file with working XSS popups

Shows how payloads execute in victim browsers

Includes educational explanations

## SQL Injection Demo
Generates data extraction reports

Shows stolen credentials and database information

Demonstrates real attack impact

## Redirect Attack Demo
Simulates open redirect vulnerabilities

Shows phishing attack scenarios

Includes live redirect demonstrations

## 🎨 Interface Overview
text
swat> help

Core Commands:
    help                    Show this help menu
    banner                  Show the SWAT banner
    exit                    Exit the framework
    clear                   Clear the screen
    show modules            List all available modules

Module Commands:
    use <module>           Use a specific module
    set TARGET <domain>    Set target domain
    run                    Execute current module
    
## 🎯 Recommended Test Targets
For legal practice, use these intentionally vulnerable applications:

Altoro Mutual: testfire.net (Demo banking app)

OWASP Juice Shop: juice-shop.herokuapp.com

bWAPP: Download and run locally

DVWA: Download and run locally

## ⚠️ Legal & Ethical Usage
🚨 IMPORTANT DISCLAIMER
This tool is for educational and authorized testing purposes only.

✅ Legal Usage
Testing your own applications

Bug bounty programs with explicit permission

Educational environments and CTF competitions

Security research with proper authorization

## ❌ Illegal Usage
Scanning websites without explicit permission

Attacking systems you don't own

Malicious hacking activities

Any unauthorized security testing

## Legal Notice
The developers and contributors are not responsible for any misuse of this tool. Users are solely responsible for ensuring they have proper authorization before conducting any security testing. Unauthorized testing may violate laws and result in criminal charges.

## 🛡️Responsible Disclosure
If you discover vulnerabilities using this tool:

Get permission before testing

Report findings responsibly to the organization

Follow disclosure guidelines and legal requirements

Never exploit vulnerabilities without authorization


## 🤝 Contributing
We welcome contributions! Please:

Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request


## 🙏 Acknowledgments
Inspired by Metasploit framework interface

Test targets provided by OWASP and security communities

Built for educational purposes in cybersecurity



Remember: With great power comes great responsibility. Use this tool ethically and legally.


