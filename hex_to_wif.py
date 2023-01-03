#!/usr/bin/env python3
# simple converter - takes a file with hex numbers
# returns a file with WIF private keys
# if a string cannot be converted to WIF, adds a line with appropriate message
# usage: python3 hex_to_wif.py <path/to/src> <path/to/dest>

import sys

import base58

from sha256 import sha256  # https://github.com/karpathy/cryptos/tree/main/cryptos


N_CURVE = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


def valid_key(key_s: str) -> bool:
    try:
        key_h = int(key_s, 16)
    except ValueError:
        return False
    if key_h <= 0 or key_h >= N_CURVE:
        return False
    return True


def hex_to_wif(key: str, *, uncompressed: bool = False) -> str:
    '''
    Converts a hexadecimal number to a WIF - private key_hex
    '''
    if not valid_key(key):
        return f"Invalid Scalar/Private Key ({key}) Skipped..."
    private_b = bytes.fromhex(
        f"80{key.lstrip('0x'):0>64}" if uncompressed else f"80{key.lstrip('0x'):0>64}01")
    private_b = private_b + sha256(sha256(private_b))[:4]
    private_wif = base58.b58encode(private_b).decode("UTF-8")
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
            file.write(hex_to_wif(hex_key) + '\n')


if __name__ == '__main__':
    main()
