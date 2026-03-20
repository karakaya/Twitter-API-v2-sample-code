"""
Delete Webhook - X API v2
=========================
Endpoint: DELETE https://api.x.com/2/webhooks/:webhook_id
Docs: https://docs.x.com/x-api/webhooks/introduction

Deletes a registered webhook. After deletion, X will stop delivering events
to the associated URL. Use list_webhooks.py to find your webhook_id.

Authentication: Bearer Token (App-only)
Required env vars: BEARER_TOKEN
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

# Replace with the webhook ID you wish to delete.
# You can find your webhook IDs by running list_webhooks.py
webhook_id = "your-webhook-id"

def main():
    response = client.webhooks.delete(webhook_id)

    print("Response code: 200")
    print(json.dumps(response.data, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
