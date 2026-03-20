"""
Create Activity Subscription - X API v2
========================================
Endpoint: POST https://api.x.com/2/activity/subscriptions
Docs: https://docs.x.com/x-api/activity/introduction

Creates a subscription to receive real-time activity events for a specified
event type and filter. Once created, matching events will be delivered to the
activity stream (see stream_events.py) and optionally to a registered webhook.

Supported public event types include:
  - profile.update.bio
  - profile.update.picture
  - profile.update.banner
  - profile.update.location
  - profile.update.url
  - profile.update.username

Authentication: Bearer Token (App-only)
Required env vars: BEARER_TOKEN
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

# Replace with the user ID you want to monitor for activity events
user_id = "2244994945"

# Replace with the event type you want to subscribe to.
# See the supported event types listed in the docstring above.
event_type = "profile.update.bio"

# Optional: replace with a registered webhook ID to also receive events via webhook delivery.
# If omitted, events are only available on the activity stream.
webhook_id = None

def main():
    payload = {
        "event_type": event_type,
        "filter": {
            "user_id": user_id
        }
    }

    # Attach a label to help identify this subscription in the stream
    payload["tag"] = f"{event_type} for user {user_id}"

    # Optionally route events to a registered webhook in addition to the stream
    if webhook_id:
        payload["webhook_id"] = webhook_id

    response = client.activity.create_subscription(body=payload)

    print("Response code: 201")
    print(json.dumps(response.data, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
