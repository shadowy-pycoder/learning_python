#!/usr/bin/env python3
# a small script showing on of the ways to calculate bitcoin block header hash
# Reference: https://en.bitcoin.it/wiki/Block_hashing_algorithm

import hashlib

import requests

height = '784952'
response = requests.get(
    f'https://api.blockchair.com/bitcoin/raw/block/{height}')
if response.status_code == 200:
    block = response.json()['data'][height]['decoded_raw_block']
    block_dict = {
        'version': int(block['versionHex'], 16).to_bytes(4, 'little'),
        'prev_block': int(block['previousblockhash'], 16).to_bytes(32, 'little'),
        'merkle_root': int(block['merkleroot'], 16).to_bytes(32, 'little'),
        'time': int(block['time']).to_bytes(4, 'little'),
        'bits': int(block['bits'], 16).to_bytes(4, 'little'),
        'nonce': int(block['nonce']).to_bytes(4, 'little')
    }

header_bin = b''.join(chunk for chunk in block_dict.values())
header_hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()[::-1].hex()
print(header_hash)
assert header_hash == block['hash']
