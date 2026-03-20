"""
Validate Webhook (Trigger CRC) - X API v2
==========================================
Endpoint: PUT https://api.x.com/2/webhooks/:webhook_id
Docs: https://docs.x.com/x-api/webhooks/introduction

Manually triggers a CRC (Challenge-Response Check) for the specified webhook.
Use this to re-validate your server's ownership or to re-enable a webhook that
was disabled due to failed CRC checks. Your webhook server must be running and
able to respond to the challenge before calling this endpoint.

Authentication: Bearer Token (App-only)
Required env vars: BEARER_TOKEN
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

# Replace with the webhook ID you wish to validate.
# You can find your webhook IDs by running list_webhooks.py
webhook_id = "your-webhook-id"

def main():
    response = client.webhooks.validate(webhook_id)

    print("Response code: 200")
    print(json.dumps(response.data, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
