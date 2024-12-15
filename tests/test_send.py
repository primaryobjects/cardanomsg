import os
import sys

# Add the parent directory of cardanomsg to the PYTHONPATH
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cardanomsg.transaction import send_message

# Create a .env file with your settings.
blockfrost_project_id = os.getenv("BlockFrostProjectId")
skey_path_name = os.getenv("SenderSecretPathName")
recipient_address = os.getenv("RecipientAddress")

# Send a transaction with the message "Hello World".
transaction_hash = send_message(blockfrost_project_id, skey_path_name, recipient_address, 1000000, "Hello World")
print(f"Transaction submitted: https://preview.cardanoscan.io/transaction/{transaction_hash}?tab=metadata")