import os
import sys

# Add the parent directory of cardanomsg to the PYTHONPATH
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cardanomsg.wallet import create

# Create a wallet.
result = create()
print(result)