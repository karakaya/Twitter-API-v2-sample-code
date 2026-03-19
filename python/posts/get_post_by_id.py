"""
Single Post Lookup - X API v2
=============================
Endpoint: GET https://api.x.com/2/tweets/:id
Docs: https://developer.x.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets-id

Authentication: Bearer Token (App-only) or OAuth (User Context)
Required env vars: BEARER_TOKEN
"""

import os
import json
from xdk import Client

bearer_token = os.environ.get("BEARER_TOKEN")
client = Client(bearer_token=bearer_token)

# Replace with the Post ID you want to look up
post_id = "post-id"

def main():
    # Post fields are adjustable. Options include:
    # attachments, author_id, context_annotations, conversation_id,
    # created_at, entities, geo, id, in_reply_to_user_id, lang,
    # non_public_metrics, organic_metrics, possibly_sensitive,
    # promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    response = client.posts.get_by_id(
        post_id,
        tweet_fields=["created_at", "author_id", "lang", "source", "public_metrics", "entities"]
    )

    print(json.dumps(response.data, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
