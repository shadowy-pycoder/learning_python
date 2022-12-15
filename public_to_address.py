#!/usr/bin/env python3
# simple converter - takes a file with bitcoin public keys
# returns a file with legacy addresses
# usage: python3 public_to_address.py <path/to/src> <path/to/dest>

import base58
import sys

from ripemd160 import ripemd160
from sha256 import sha256


def public_address(key):
    key = bytes.fromhex(key)
    address = bytes.fromhex(f"00{ripemd160(sha256(key)).hex()}")
    checksum = sha256(sha256(address))
    address = f"{address.hex()}{checksum.hex()[:8]}"
    address = base58.b58encode(bytes.fromhex(address)).decode("UTF-8")
    return address


if len(sys.argv) < 3:
    print('Usage: app.py <path/to/src> <path/to/dest>')
    sys.exit(1)

path_src = sys.argv[1]
path_dest = sys.argv[2]
addresses = []

with open(path_src, 'r', encoding='UTF-8') as file:
    pub_keys = file.readlines()

pub_keys = (pub_key.strip() for pub_key in pub_keys)

for pub_key in pub_keys:
    addr = public_address(pub_key)
    addresses.append(addr)

with open(path_dest, 'w', encoding='UTF-8') as file:
    for address in addresses:
        file.write(address + '\n')
