# cardanomsg/transaction.py

import json
from blockfrost import ApiUrls
from pycardano import *

def send_ada_message(blockfrost_project_id, skey_path_name, recipient_address, amount, message, network = Network.TESTNET):
    # Load the signing key using pycardano
    with open(skey_path_name, "r") as f:
        skey_data = json.load(f)
        psk = PaymentSigningKey.from_primitive(bytes.fromhex(skey_data["cborHex"]))

    # Create the signing key from the secret key
    pvk = PaymentVerificationKey.from_signing_key(psk)

    # Derive an address
    address = Address(pvk.hash(), network=network)

    # Create a BlockFrost chain context
    context = BlockFrostChainContext(blockfrost_project_id, base_url=ApiUrls.preview.value)

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
    metadata[1] = message

    # Create auxiliary data with the metadata
    auxiliary_data = AuxiliaryData(data=metadata)

    # Add auxiliary data to the transaction builder
    builder.auxiliary_data = auxiliary_data

    # Sign and submit the transaction
    signed_tx = builder.build_and_sign([psk], change_address=address)
    context.submit_tx(signed_tx)

    # Return the transaction hash
    return signed_tx.id
