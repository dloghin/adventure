from ecpy.curves import Curve
from ecpy.keys import ECPublicKey, ECPrivateKey
from sha3 import keccak_256
import sys

def pk2addr(private_key):
    private_key = private_key.strip().lower()
    if not private_key.startswith('0x'):
        private_key = '0x' + private_key

    cv = Curve.get_curve('secp256k1')
    pv_key = ECPrivateKey(int(private_key, 16), cv)
    pu_key = pv_key.get_public_key()

    concat_x_y = pu_key.W.x.to_bytes(32, byteorder='big') + pu_key.W.y.to_bytes(32, byteorder='big')
    eth_addr = '0x' + keccak_256(concat_x_y).digest()[-20:].hex()
    return eth_addr


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pk2addr.py <private_key>")
        exit(1)

    eth_addr = pk2addr(sys.argv[1])

    # print('private key: ', hex(private_key))
    print(eth_addr)

