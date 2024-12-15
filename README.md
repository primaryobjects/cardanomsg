# cardanomsg

Send ADA with a message in the metadata using the Cardano blockchain.

## Installation

You can install the module using pip:

```sh
pip install cardanomsg
```

## Usage

A [BlockFrost](https://blockfrost.io/) API account is required *(to prevent needing to run the blockchain locally on your PC)*.

## Send message

Send a message in a transaction.

```python
from cardanomsg.transaction import send_message
transaction_hash = send_message("<BLOCKFROST_PROJECT_ID>", "wallet.skey", "<RECIPIENT_ADDRESS>", 1000000, "Hello World")
```

## Get message

Get a message from a transaction.

```python
from cardanomsg.transaction import get_message
message = get_message("<BLOCKFROST_PROJECT_ID>", "079112f6a5192c6eeae57de0607d61e07dea864efc2bbad7aa953795a5c56aae")[0].json_metadata
```

You can also view the message on the blockchain using Cardanoscan.

https://preview.cardanoscan.io/transaction/079112f6a5192c6eeae57de0607d61e07dea864efc2bbad7aa953795a5c56aae?tab=metadata

```
Summary | UTXOs | Metadata (1)

Metadata Hash: 2f86fa9fdfcb606ab2b5f060bd125848e45187cf2c798ab389e6a9af98ba8ad1
Public Label: 1
Value: "Hello World"
```

## Create wallet

Create a wallet.

```
from cardanomsg.wallet import create
result = create()
```

Two files will be created: `wallet.skey` and `wallet.addr`.

The contents of `wallet.skey` is the secret key with the following format.

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