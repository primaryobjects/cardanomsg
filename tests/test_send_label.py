import os
import sys
import uuid

# Add the parent directory of cardanomsg to the PYTHONPATH
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cardanomsg.transaction import send_message

# Create a .env file with your settings.
blockfrost_project_id = os.getenv("BlockFrostProjectId")
skey_path_name = os.getenv("SenderSecretPathName")
recipient_address = os.getenv("RecipientAddress")

# Generate a label as a random number.
label = uuid.uuid4().int & (1<<32)-1

# Send a transaction with the message "Hello World".
payload = {
    "id": 12345,
    "text": "Hello World"
}

# Submit the transaction.
transaction_hash = send_message(blockfrost_project_id, skey_path_name, recipient_address, 1000000, payload, label)
print(f"Transaction submitted: https://preview.cardanoscan.io/transaction/{transaction_hash}?tab=metadata")

# The metadata can be searched using the label (wait 1-3 minutes for the transaction to complete).
# message = find_message(blockfrost_project_id, label)
# print(message[0].json_metadata)