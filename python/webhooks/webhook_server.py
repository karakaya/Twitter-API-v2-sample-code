"""
Webhook Server - X API v2
=========================
Docs: https://docs.x.com/x-api/webhooks/introduction

This is a minimal webhook consumer server that handles two responsibilities:
  1. CRC (Challenge-Response Check) validation via GET — X sends a crc_token
     and expects back an HMAC-SHA256 hash signed with your Consumer Secret.
     This is required when registering a webhook and periodically thereafter
     to confirm your server is still alive.
  2. Event delivery via POST — X sends account activity or filtered stream
     events as JSON payloads to this endpoint in real time.

To receive events you must:
  1. Run this server at a publicly accessible HTTPS URL (e.g. via ngrok).
  2. Register the URL with X: see register_webhook.py
  3. Subscribe user accounts or set stream rules to start receiving events.

Authentication: Consumer Secret (HMAC-SHA256 for CRC validation)
Required env vars: CONSUMER_SECRET
Dependencies: flask, waitress (pip install flask waitress)
"""

import base64
import hashlib
import hmac
import json
import os
import sys

from flask import Flask, jsonify, request
from waitress import serve

app = Flask(__name__)

# Your app's Consumer Secret — used to sign the CRC response.
# To set environment variables on macOS or Linux, run the export commands below from the terminal:
# export CONSUMER_SECRET='YOUR-CONSUMER-SECRET'
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
if CONSUMER_SECRET is None:
    print("Missing consumer secret. Ensure CONSUMER_SECRET env var is set.")
    sys.exit(1)

HOST = "0.0.0.0"
PORT = 8080


@app.route('/webhooks', methods=['GET', 'POST'])
def webhook_request():
    # Handle GET request (CRC challenge)
    if request.method == 'GET':
        crc_token = request.args.get('crc_token')
        print(f"CRC Token received: {crc_token}")

        if crc_token is None:
            print("Error: No crc_token found in the request.")
            return jsonify({'error': 'No crc_token'}), 400

        # Creates HMAC SHA-256 hash from the incoming token and your Consumer Secret
        sha256_hash_digest = hmac.new(
            CONSUMER_SECRET.encode('utf-8'),
            msg=crc_token.encode('utf-8'),
            digestmod=hashlib.sha256
        ).digest()

        # Construct response data with base64 encoded hash
        response = {
            'response_token': 'sha256=' + base64.b64encode(sha256_hash_digest).decode('utf-8')
        }

        # Returns properly formatted json response
        return jsonify(response)

    # Handle POST request (webhook event delivery)
    elif request.method == 'POST':
        event_data = request.get_json()
        if event_data:
            print(json.dumps(event_data, indent=2))
        else:
            # Log if the request body wasn't JSON or was empty
            print(f"Body: {request.data.decode('utf-8')}")

        # Return 200 OK immediately to acknowledge receipt.
        # X will retry delivery if it does not receive a 2xx response promptly.
        return '', 200

    return 'Method Not Allowed', 405


def main():
    print("--- Starting Webhook Server ---")
    print(f"Listening on {HOST}:{PORT}")
    print("Expose this server publicly (e.g. via ngrok) then register the URL with register_webhook.py")
    serve(app, host=HOST, port=PORT)


if __name__ == '__main__':
    main()
