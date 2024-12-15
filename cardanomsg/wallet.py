# cardanomsg/wallet.py

import json
from pycardano import PaymentSigningKey, PaymentVerificationKey, Address, Network

def create(network = Network.TESTNET):
    # Generates a wallet address using pycardano.

    # Generate a new payment signing key
    psk = PaymentSigningKey.generate()

    # Derive the corresponding payment verification key
    pvk = PaymentVerificationKey.from_signing_key(psk)

    # Derive the address
    address = Address(pvk.hash(), network=network)

    # Create the JSON structure for the secret key
    skey_data = {
        "type": "PaymentSigningKeyShelley_ed25519",
        "description": "Payment Signing Key",
        "cborHex": psk.to_primitive().hex()
    }

    # Save the secret key to a file
    with open("wallet.skey", "w") as f:
        json.dump(skey_data, f, indent=2)

    # Save the generated address to a file
    with open("wallet.addr", "w") as f:
        f.write(str(address))

    return (address, 'wallet.skey', 'wallet.addr')