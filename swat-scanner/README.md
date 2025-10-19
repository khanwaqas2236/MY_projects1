# SWAT - Security Web Assessment Tool

![SWAT Banner](https://img.shields.io/badge/SWAT-Web%20Security%20Tool-red)
![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A powerful Metasploit-style web vulnerability scanner with interactive exploitation demonstrations.

## 🚀 Features

- **Metasploit-style Interface**: Professional command-line interface
- **Multiple Scan Modules**: Subdomain enumeration, XSS, SQL injection, redirect checks
- **Visible Exploitation**: Generate HTML demos showing actual attack proofs
- **Educational Tool**: Perfect for learning web application security
- **Ethical Framework**: Built with responsible disclosure in mind

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/swat-scanner.git
cd swat-scanner

# Install dependencies
pip install -r requirements.txt

# Run the tool
python swat_scanner.py

## Usage
# Start the tool
python swat_scanner.py

# Basic commands
swat> show modules
swat> use xss_scanner
swat(xss_scanner)> set TARGET testfire.net
swat(xss_scanner)> run

🛡️ Legal & Ethical Use
⚠️ IMPORTANT: Only use on websites you own or have explicit permission to test.

## Authorized testing domains:

testfire.net (Altoro Mutual - Demo Bank)

juice-shop.herokuapp.com (OWASP Juice Shop)

Your own local applications

## 🎪 Demo Attacks
The tool generates interactive HTML files demonstrating:

XSS Popups: JavaScript alert boxes

SQL Injection: Data extraction reports

Redirect Attacks: Phishing simulations

Full Attack Chains: Comprehensive demonstrations
