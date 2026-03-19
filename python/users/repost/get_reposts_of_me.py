"""
Reposts of Me - X API v2
=========================
Endpoint: GET https://api.x.com/2/users/reposts_of_me
Docs: https://docs.x.com/x-api/users/get-reposts-of-me

Authentication: OAuth 2.0 (User Context)
Required env vars: CLIENT_ID, CLIENT_SECRET

Note: Returns posts from the authenticated user's timeline that have been reposted.
"""

import os
import json
from xdk import Client
from xdk.oauth2_auth import OAuth2PKCEAuth

# The code below sets the client ID and client secret from your environment variables
# To set environment variables on macOS or Linux, run the export commands below from the terminal:
# export CLIENT_ID='YOUR-CLIENT-ID'
# export CLIENT_SECRET='YOUR-CLIENT-SECRET'
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Replace the following URL with your callback URL, which can be obtained from your App's auth settings.
redirect_uri = "https://example.com"

# Set the scopes
scopes = ["tweet.read", "users.read", "offline.access"]

def main():
    # Step 1: Create PKCE instance
    auth = OAuth2PKCEAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scopes
    )

    # Step 2: Get authorization URL
    auth_url = auth.get_authorization_url()
    print("Visit the following URL to authorize your App on behalf of your X handle in a browser:")
    print(auth_url)

    # Step 3: Handle callback
    callback_url = input("Paste the full callback URL here: ")

    # Step 4: Exchange code for tokens
    tokens = auth.fetch_token(authorization_response=callback_url)
    access_token = tokens["access_token"]

    # Step 5: Create client
    client = Client(access_token=access_token)

    # Step 6: Get the authenticated user's posts that have been reposted
    # Post fields are adjustable. Options include:
    # attachments, author_id, context_annotations, conversation_id,
    # created_at, entities, geo, id, in_reply_to_user_id, lang,
    # non_public_metrics, organic_metrics, possibly_sensitive,
    # promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    all_posts = []
    for page in client.users.get_reposts_of_me(
        max_results=100,
        tweet_fields=["created_at", "public_metrics"]
    ):
        # Access data attribute (model uses extra='allow' so data should be available)
        # Use getattr with fallback in case data field is missing from response
        page_data = getattr(page, 'data', []) or []
        all_posts.extend(page_data)
        print(f"Fetched {len(page_data)} posts (total: {len(all_posts)})")

    print(f"\nTotal Reposted Posts: {len(all_posts)}")
    print(json.dumps({"data": all_posts[:5]}, indent=4, sort_keys=True))  # Print first 5 as example


if __name__ == "__main__":
    main()
