import os
import sys

# Add the parent directory of cardanomsg to the PYTHONPATH
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cardanomsg.transaction import get_message

# Create a .env file with your settings.
blockfrost_project_id = os.getenv("BlockFrostProjectId")

# Load a message from the blockchain.
message = get_message(blockfrost_project_id, "079112f6a5192c6eeae57de0607d61e07dea864efc2bbad7aa953795a5c56aae")[0].json_metadata
print(message)