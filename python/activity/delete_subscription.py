"""
Delete Activity Subscription - X API v2
========================================
Endpoint: DELETE https://api.x.com/2/activity/subscriptions/:id
Docs: https://docs.x.com/x-api/activity/introduction

Deletes an activity subscription. Once deleted, events matching that subscription
will no longer be delivered to the stream or associated webhook. Use
list_subscriptions.py to find the subscription_id you wish to remove.

Authentication: Bearer Token (App-only)
Required env vars: BEARER_TOKEN
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

# Replace with the subscription ID you wish to delete.
# You can find subscription IDs by running list_subscriptions.py
subscription_id = "your-subscription-id"

def main():
    response = client.activity.delete_subscription(subscription_id)

    print("Response code: 200")
    print(json.dumps(response.data, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
