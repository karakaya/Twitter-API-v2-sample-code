"""
List Activity Subscriptions - X API v2
=======================================
Endpoint: GET https://api.x.com/2/activity/subscriptions
Docs: https://docs.x.com/x-api/activity/introduction

Returns all active activity subscriptions for your app. Use the subscription_id
from the response to update or delete individual subscriptions.

Authentication: Bearer Token (App-only)
Required env vars: BEARER_TOKEN
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

def main():
    response = client.activity.get_subscriptions()

    # Access data attribute safely
    response_data = getattr(response, 'data', None)
    if response_data:
        print(json.dumps(response_data, indent=4, sort_keys=True))
    else:
        print(json.dumps(response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
