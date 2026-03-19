"""
Update Activity Subscription - X API v2
========================================
Endpoint: PUT https://api.x.com/2/activity/subscriptions/:id
Docs: https://docs.x.com/x-api/activity/introduction

Updates an existing activity subscription. You can change the filter (e.g. target
a different user ID), the tag, or the associated webhook. Use list_subscriptions.py
to find the subscription_id you wish to update.

Authentication: Bearer Token (App-only)
Required env vars: BEARER_TOKEN
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

# Replace with the subscription ID you wish to update.
# You can find subscription IDs by running list_subscriptions.py
subscription_id = "your-subscription-id"

# Replace with the updated user ID you want to monitor
updated_user_id = "2244994945"

def main():
    payload = {
        "filter": {
            "user_id": updated_user_id
        }
    }

    response = client.activity.update_subscription(subscription_id, body=payload)

    print("Response code: 200")
    print(json.dumps(response.data, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
