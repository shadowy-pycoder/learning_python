#!/usr/bin/env python3
# simple converter - takes a file with bitcoin public keys
# returns a file with legacy addresses
# usage: python3 public_to_address.py <path/to/src> <path/to/dest>

import base58
import sys

from ripemd160 import ripemd160
from sha256 import sha256


def public_address(key: str) -> str:
    address = b'\x00' + ripemd160(sha256(bytes.fromhex(key)))
    checksum = sha256(sha256(address))[:4]
    return base58.b58encode(address + checksum).decode("UTF-8")


def main():
    if len(sys.argv) < 3:
        print('Usage: app.py <path/to/src> <path/to/dest>')
        sys.exit(1)

    path_src = sys.argv[1]
    path_dest = sys.argv[2]

    with open(path_src, 'r', encoding='UTF-8') as file:
        pub_keys = file.read().splitlines()

    with open(path_dest, 'w', encoding='UTF-8') as file:
        for pub_key in pub_keys:
            file.write(public_address(pub_key) + '\n')


if __name__ == '__main__':
    main()

