# SWAT - Security Web Assessment Tool

                                  ███████╗██╗    ██╗ █████╗ ████████╗
                                  ██╔════╝██║    ██║██╔══██╗╚══██╔══╝
                                  ███████╗██║ █╗ ██║███████║   ██║   
                             ╚══  ═   ═██║██║███╗██║██╔══██║   ██║   
                                  ███████║╚███╔███╔╝██║  ██║   ██║   
                                  ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝ 



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

# HELP & NAVIGATION COMMANDS
swat> help                    # Show all commands

swat> banner                  # Show SWAT banner

swat> clear                   # Clear screen

swat> show modules            # List all available modules

swat> exit                    # Quit the tool

# Subdomain Discovery

swat> use subdomain_enum

swat(subdomain_enum)> set TARGET example.com

swat(subdomain_enum)> run

# XSS Scanning

swat> use xss_scanner

swat(xss_scanner)> set TARGET example.com

swat(xss_scanner)> run

# SQL Injection Scanning

swat> use sqli_detector

swat(sqli_detector)> set TARGET example.com

swat(sqli_detector)> run

# Redirect Vulnerability Scanning

swat> use redirect_check

swat(redirect_check)> set TARGET example.com

swat(redirect_check)> run

# Full Comprehensive Audit

swat> use full_audit

swat(full_audit)> set TARGET example.com

swat(full_audit)> run

# 🎪 EXPLOITATION COMMANDS

[?] Do you want to proceed with exploitation? (yes/no): yes

## 🚨 QUICK START EXAMPLE

# 1. Start tool
python swat_scanner.py

# 2. Show modules
swat> show modules

# 3. Use XSS scanner
swat> use xss_scanner

# 4. Set target
swat(xss_scanner)> set TARGET testfire.net

# 5. Run scan
swat(xss_scanner)> run

# 6. Exploit when asked

[?] Do you want to proceed with exploitation? (yes/no): yes

# 7. Choose demo type

Enter choice (1-4): 1

xss_scanner - Cross-Site Scripting detection

sqli_detector - SQL Injection vulnerability scanning

redirect_check - Open redirect vulnerability checks

full_audit - Comprehensive web application audit

## 🛠️ Usage Examples

Example 1: Full Website Audit


swat> use full_audit

swat(full_audit)> set TARGET example.com

swat(full_audit)> run

## Example 2: SQL Injection Testing

swat> use sqli_detector

swat(sqli_detector)> set TARGET testphp.vulnweb.com

swat(sqli_detector)> run

Example 3: Subdomain Discovery

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


