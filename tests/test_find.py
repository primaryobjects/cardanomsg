import os
import sys

# Add the parent directory of cardanomsg to the PYTHONPATH
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cardanomsg.transaction import find_message

# Create a .env file with your settings.
blockfrost_project_id = os.getenv("BlockFrostProjectId")

# Load a string from the blockchain under the specified label.
message = find_message(blockfrost_project_id, 3837929064)
print(f"Find string: {message[1].json_metadata}")

# Load a single JSON object from the blockchain under the specified label.
message = find_message(blockfrost_project_id, 1782959986)
print(f"Find JSON object: {message[0].json_metadata}")

# Load multiple JSON objects from the blockchain under the specified label.
messages = find_message(blockfrost_project_id, 3648849023)
print("Find multiple JSON objects:")
for message in messages:
    print(message.json_metadata)