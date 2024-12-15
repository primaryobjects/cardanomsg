# cardanomsg

Send ADA with a message in the metadata using the Cardano blockchain.

## Installation

You can install the module using pip:

```sh
pip install cardanomsg
```

## Usage

A [BlockFrost](https://blockfrost.io/) API account is required *(to prevent needing to run the blockchain locally on your PC)*.

```python
from cardanomsg.transaction import send_ada_message

blockfrost_project_id = "your_blockfrost_project_id"
skey_path_name = "path_to_your_secret_json_key_file"
recipient_address = "your_recipient_address"

transaction_hash = send_ada_message(blockfrost_project_id, skey_path_name, recipient_address, 1000000, "Hello World")
```

## View the message

You can view the message on the blockchain using Cardanoscan.

https://preview.cardanoscan.io/transaction/{transaction_hash}?tab=metadata

Here is an example of the output:

```
Summary | UTXOs | Metadata (1)

Metadata Hash: 12345abcdefg606ab2b5f01298abxyz848e45187cf2c798ab389e6abcdefg
Public Label: 1
Value: "Hello World"
```

## Sender JSON file format

The secret key for the sender is [generated](https://github.com/primaryobjects/cardano-tutorial/blob/main/generate.py) by pycardano. The format contains the following:

```json
{
  "type": "PaymentSigningKeyShelley_ed25519",
  "description": "Payment Signing Key",
  "cborHex": "<SENDER_SECRET_KEY>"
}
```

## License

MIT

## Author

Kory Becker
http://primaryobjects.com