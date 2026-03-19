"""
List Webhooks - X API v2
========================
Endpoint: GET https://api.x.com/2/webhooks
Docs: https://docs.x.com/x-api/webhooks/introduction

Returns all registered webhooks for your app. Use the webhook_id from the
response when managing subscriptions or deleting a webhook.

Authentication: Bearer Token (App-only)
Required env vars: BEARER_TOKEN
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

def main():
    response = client.webhooks.get()

    print(json.dumps(response.data, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
