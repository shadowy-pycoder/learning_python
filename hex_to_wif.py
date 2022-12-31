#!/usr/bin/env python3
# simple converter - takes a file with hex numbers
# returns a file with WIF private keys
# if a string cannot be converted to WIF, adds a line with appropriate message
# usage: python3 hex_to_wif.py <path/to/src> <path/to/dest>

import sys

import base58

from sha256 import sha256  # https://github.com/karpathy/cryptos/tree/main/cryptos


N_CURVE = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


def hex_to_wif(key: str, *, uncompressed=False) -> str:
    '''
    Converts a hexadecimal number to a WIF - private key
    '''
    try:
        key = int(key, 16)
    except ValueError:
        return f"Invalid Scalar/Private Key ({key}) Skipped..."
    if key <= 0 or key >= N_CURVE:
        return f"Invalid Scalar/Private Key ({hex(key)}) Skipped..."
    key = f"80{key:0>64x}" if uncompressed else f"80{key:0>64x}01"
    private_wif = bytes.fromhex(key)
    checksum = sha256(sha256(private_wif))
    private_wif = f"{private_wif.hex()}{checksum.hex()[:8]}"
    private_wif = base58.b58encode(
        bytes.fromhex(private_wif)).decode("UTF-8")
    return private_wif


def main():
    if len(sys.argv) < 3:
        print('Usage: app.py <path/to/src> <path/to/dest>')
        sys.exit(1)

    path_src = sys.argv[1]
    path_dest = sys.argv[2]

    with open(path_src, 'r', encoding='UTF-8') as file:
        hex_keys = file.read().splitlines()

    with open(path_dest, 'w', encoding='UTF-8') as file:
        for hex_key in hex_keys:
            file.write(hex_to_wif(hex_key, uncompressed=True) + '\n')


if __name__ == '__main__':
    main()
