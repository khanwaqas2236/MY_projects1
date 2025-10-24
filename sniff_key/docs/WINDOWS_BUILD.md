# Windows Build Guide

## Building Executable
```cmd
# Method 1: Using batch script
scripts\build.bat

# Method 2: Manual PyInstaller
pyinstaller --onefile --noconsole --icon=assets/icon.ico src/keylogger.py
