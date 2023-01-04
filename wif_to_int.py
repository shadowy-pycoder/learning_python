import base58

from sha256 import sha256

N_CURVE = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141


def valid_key(key: int) -> bool:
    return not (key <= 0 or key >= N_CURVE)


def valid_checksum(version: bytes, private_key: bytes, checksum: bytes) -> bool:
    return sha256(sha256(version + private_key))[:4] == checksum


def wif_to_bytes(wif: str) -> tuple[bytes, ...]:
    private_key = base58.b58decode(wif)
    return private_key[:1], private_key[1:-4], private_key[-4:]


def wif_to_int(wif: str) -> int:
    # https://en.bitcoin.it/wiki/Wallet_import_format
    version, private_key, checksum = wif_to_bytes(wif)
    if not valid_checksum(version, private_key, checksum):
        raise ValueError("Invalid WIF checksum")
    private_key_int = int.from_bytes(private_key[:-1], 'big') if len(
        private_key) == 33 else int.from_bytes(private_key, 'big')
    return private_key_int if valid_key(private_key_int) else -1
