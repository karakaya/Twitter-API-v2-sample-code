"""
Register Webhook - X API v2
===========================
Endpoint: POST https://api.x.com/2/webhooks
Docs: https://docs.x.com/x-api/webhooks/introduction

Registers a new webhook URL with X. When you make this request, X immediately
sends a CRC challenge GET request to your URL to verify ownership. Your server
must respond correctly before the webhook is saved — see webhook_server.py.

Authentication: Bearer Token (App-only)
Required env vars: BEARER_TOKEN
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

# Replace with your publicly accessible HTTPS webhook URL.
# The URL must be reachable by X at the time of registration so the CRC check can complete.
# For local development you can use a tool like ngrok to expose a local server.
webhook_url = "https://your-domain.com/webhooks"

def main():
    payload = {"url": webhook_url}
    response = client.webhooks.create(body=payload)

    print("Response code: 200")
    print(json.dumps(response.data, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
