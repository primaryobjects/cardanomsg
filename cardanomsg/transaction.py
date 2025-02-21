# cardanomsg/transaction.py

import json
from blockfrost import ApiUrls, BlockFrostApi, ApiError
from pycardano import *

def send_message(blockfrost_project_id, skey_path_name, recipient_address, amount, message, label = 1, network = Network.TESTNET):
    """
    Sends a transaction of ADA from sender to recipient and creates a message in the transaction metadata. The resulting message is viewable on the blockchain.
    Params:
    blockfrost_project_id: Your BlockFrost Project ID
    skey_path_name: File path to your wallet's secret json file. Use cardanomsg.wallet.create to generate one.
    recipient_address: Wallet address of the recipient.
    amount: Amount in lovelace to send to recipient along with message. 1 ADA = 1000000 lovelace
    message: Text message or JSON object to embed in the transaction metadata.
    label: A numeric searchable label to use for the message metadata. Default is 1.
    network: Network.TESTNET or Network.MAINNET
    """

    # Load the signing key using pycardano
    with open(skey_path_name, "r") as f:
        skey_data = json.load(f)
        psk = PaymentSigningKey.from_primitive(bytes.fromhex(skey_data["cborHex"]))

    # Create the signing key from the secret key
    pvk = PaymentVerificationKey.from_signing_key(psk)

    # Derive an address
    address = Address(pvk.hash(), network=network)

    # Create a BlockFrost chain context
    network_urls = {
        Network.MAINNET: ApiUrls.mainnet.value,
        Network.TESTNET: ApiUrls.preview.value
    }
    api_base_url = network_urls[network]
    context = BlockFrostChainContext(blockfrost_project_id, base_url=api_base_url)

    # Create a transaction builder
    builder = TransactionBuilder(context)

    # Add input address
    builder.add_input_address(address)

    # Get all UTxOs at this address
    utxos = context.utxos(address)

    # Add a specific UTxO to the transaction
    builder.add_input(utxos[0])

    # Add an output without a datum hash
    builder.add_output(
        TransactionOutput(
            Address.from_primitive(recipient_address),
            Value.from_primitive([amount])
        )
    )

    # Build the transaction
    tx = builder.build()

    # Create metadata with the message
    metadata = Metadata()

    # Store as metadata (JSON object or text).
    metadata[label] = message

    # Create auxiliary data with the metadata
    auxiliary_data = AuxiliaryData(data=metadata)

    # Add auxiliary data to the transaction builder
    builder.auxiliary_data = auxiliary_data

    # Sign and submit the transaction
    signed_tx = builder.build_and_sign([psk], change_address=address)
    context.submit_tx(signed_tx)

    # Return the transaction hash
    return signed_tx.id

def get_message(blockfrost_project_id, transaction_hash, api = ApiUrls.preview):
    """
    Displays metadata from a blockchain transaction.
    Params:
    blockfrost_project_id: Your BlockFrost Project ID
    transaction_hash: Transaction hash from sending a transaction using cardanomsg.transaction.send_message
    api: BlockFrost API endpoint, includes ApiUrls.preview, ApiUrls.mainnet, ApiUrls.testnet
    """

    api = BlockFrostApi(project_id=blockfrost_project_id, base_url=api.value)

    # Fetch the transaction metadata
    return api.transaction_metadata(transaction_hash)

def find_message(blockfrost_project_id, label, api = ApiUrls.preview):
    """
    Returns metadata from all transactions using a specific label.
    Params:
    blockfrost_project_id: Your BlockFrost Project ID
    label: The numeric metadata label to search for
    api: BlockFrost API endpoint, includes ApiUrls.preview, ApiUrls.mainnet, ApiUrls.testnet
    """
    api = BlockFrostApi(project_id=blockfrost_project_id, base_url=api.value)

    # Fetch the transaction metadata
    try:
        return api.metadata_label_json(label)
    except ApiError as ex:
        if ex.status_code == 404:
            return None
