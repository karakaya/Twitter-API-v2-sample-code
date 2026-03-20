"""
Unfollow User - X API v2
========================
Endpoint: DELETE https://api.x.com/2/users/:source_user_id/following/:target_user_id
Docs: https://developer.x.com/en/docs/twitter-api/users/follows/api-reference/delete-users-source_user_id-following

Authentication: OAuth 2.0 (User Context)
Required env vars: CLIENT_ID, CLIENT_SECRET
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
scopes = ["tweet.read", "users.read", "follows.write", "offline.access"]

# Be sure to replace user-id-to-unfollow with the id of the user you wish to unfollow.
# You can find a user ID by using the user lookup endpoint
target_user_id = "user-id-to-unfollow"

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

    # Step 6: Get the authenticated user's ID
    me_response = client.users.get_me()
    user_id = me_response.data["id"]

    # Step 7: Unfollow the user
    response = client.users.unfollow_user(user_id, target_user_id)

    print("Response code: 200")
    print(json.dumps(response.data, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
