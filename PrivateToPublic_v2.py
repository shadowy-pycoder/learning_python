import base58  # pip install base58

# these modules are taken from here https://github.com/karpathy/cryptos/tree/main/cryptos
from ripemd160 import ripemd160
from sha256 import sha256


class PublicKey:

    """Calculating public key from private key"""
    """Parameters of an elliptic curve"""
    # you can find these parameters here https://en.bitcoin.it/wiki/Secp256k1 or
    # in the official specification https://www.secg.org/sec2-v2.pdf
    p_curve = (2**256 - 2**32 - 2**9 - 2**8 - 2**7 -
               2**6 - 2**4 - 1)  # The proven prime
    # Number of points in the field
    n_curve = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    # These two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
    a_curve, b_curve = 0, 7
    gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
    gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
    gpoint = (gx, gy)  # This is generator point.

    def __init__(self, private_key):

        self.private_key = private_key

    @property
    def private_key(self):
        return self.__private_key

    @private_key.setter
    def private_key(self, key):
        # catch ivalid private keys as early as possible
        try:
            key = int(str(key), 16)
        except ValueError:
            raise NotImplementedError(
                'Private key must be a hexadecimal number')
        if key <= 0 or key >= self.n_curve:
            raise Exception("Invalid Scalar/Private Key")

        self.__private_key = key

    def __modinv(self, a, n):
        """Extended Euclidean Algorithm"""
        # https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
        lm, hm = 1, 0
        low, high = a % n, n
        while low > 1:
            ratio = int(high/low)
            nm, new = int(hm-lm*ratio), int(high-low*ratio)
            lm, low, hm, high = nm, new, lm, low
        return lm % n

    def __ec_add(self, a, b):
        """Point addition"""
        # https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_addition
        lam_add = ((b[1]-a[1]) * self.__modinv(b[0] -
                   a[0], self.p_curve)) % self.p_curve
        x = (pow(lam_add, 2)-a[0]-b[0]) % self.p_curve
        y = (lam_add*(a[0]-x)-a[1]) % self.p_curve
        return x, y

    def __ec_double(self, a):
        """EC point doubling"""
        # https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Point_doubling
        lam = ((3*a[0]*a[0]+self.a_curve) *
               self.__modinv((2*a[1]), self.p_curve)) % self.p_curve
        x = int((lam*lam-2*a[0]) % self.p_curve)
        y = int((lam*(a[0]-x)-a[1]) % self.p_curve)
        return x, y

    def __ec_multiply(self, genpoint, scalarhex):
        """EC point multiplication"""
        # https://en.wikipedia.org/wiki/Elliptic_curve_point_multiplication#Double-and-add
        scalarbin = str(bin(scalarhex))[2:]
        q = genpoint
        for i in range(1, len(scalarbin)):  # Double and add to multiply point
            q = self.__ec_double(q)
            if scalarbin[i] == "1":
                q = self.__ec_add(q, genpoint)
        return q

    def __compute_public(self):
        """Calculating a public key"""
        return self.__ec_multiply(self.gpoint, self.private_key)

    def __public_address(self, key):
        """Function calculating address"""
        # steps are described here https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses
        # bytes representation is needed for sha256 and ripemd160
        key = bytes.fromhex(key)
        # Take the corresponding public key
        # Perform SHA-256 hashing on the public key
        # Perform RIPEMD-160 hashing on the result of SHA-256
        # Add version byte in front of RIPEMD-160 hash (0x00 for Main Network)
        address = bytes.fromhex(f"00{ripemd160(sha256(key)).hex()}")
        # Perform SHA-256 hash on the extended RIPEMD-160 result
        # Perform SHA-256 hash on the result of the previous SHA-256 hash
        checksum = sha256(sha256(address))
        # Take the first 4 bytes of the second SHA-256 hash. This is the address checksum
        # Add the checksum bytes at the end of extended RIPEMD-160 hash.
        # This is the 25-byte binary Bitcoin Address.
        address = f"{address.hex()}{checksum.hex()[:8]}"
        # Convert the result from a byte string into a base58 string using Base58Check encoding.
        # This is the most commonly used Bitcoin Address format
        address = base58.b58encode(bytes.fromhex(address)).decode("UTF-8")
        return address

    def __convert_private_to_wif(self):
        """Converting a private key to WIF"""

        # convert private key to bytes for sha256
        # steps are described here https://en.bitcoin.it/wiki/Wallet_import_format
        # take a private key in hex and add a 0x80 byte in front of it for mainnet addresses
        private_wif = bytes.fromhex(f"80{self.private_key:0>64x}")
        private_wif_comp = bytes.fromhex(
            f"80{self.private_key:0>64x}01")
        # Perform SHA-256 hash on the extended key.
        # Perform SHA-256 hash on result of SHA-256 hash.
        checksum = sha256(sha256(private_wif))
        checksum_comp = sha256(sha256(private_wif_comp))
        # Take the first 4 bytes of the second SHA-256 hash; this is the checksum.
        # Add the checksum bytes at the end of the extended key.
        private_wif = f"{private_wif.hex()}{checksum.hex()[:8]}"
        private_wif_comp = f"{private_wif_comp.hex()}{checksum_comp.hex()[:8]}"
        # Convert the result from a byte string into a base58 string using Base58Check encoding.
        # This is the wallet import format (WIF).
        private_wif = base58.b58encode(
            bytes.fromhex(private_wif)).decode("UTF-8")
        private_wif_comp = base58.b58encode(
            bytes.fromhex(private_wif_comp)).decode("UTF-8")

        return private_wif, private_wif_comp

    def print_private_keys(self):
        """Printing private keys in WIF"""
        priv_key, priv_key_comp = self.__convert_private_to_wif()
        priv_hex = f'0x{self.private_key:0>64x}'
        print(f"\nHEX - private key\n{priv_hex}")
        print(f"Length: {len(priv_hex)}\n")
        print(f"\nWIF - private key\n{priv_key}")
        print(f"Length: {len(priv_key)}\n")
        print(f"WIF compressed - private key\n{priv_key_comp}")
        print(f"Length: {len(priv_key_comp)}\n")

    def print_public_keys(self):
        """Printing public key in different formats"""
        public_key = self.__compute_public()
        print("\nThe uncompressed public key (not address):")
        print(public_key)
        print("\nThe uncompressed public key (HEX):")
        uncomp_pub = f"04{public_key[0]:0>64x}{public_key[1]:0>64x}"
        print(uncomp_pub)
        print(f"Length: {len(uncomp_pub)}\n")
        uncomp_addr = self.__public_address(uncomp_pub)
        print(f"Address from uncompressed key\n{uncomp_addr}")
        print("\nThe official Public Key - compressed:")
        if public_key[1] % 2 == 1:  # If the Y value for the Public Key is odd.
            comp_pub = f"03{public_key[0]:0>64x}"
        else:  # Or else, if the Y value is even.
            comp_pub = f"02{public_key[0]:0>64x}"
        print(comp_pub)
        print(f"Length: {len(comp_pub)}\n")
        comp_addr = self.__public_address(comp_pub)
        print(f"Address from compressed key\n{comp_addr}")


prompt = input(f"Please insert your private key in HEX format (0x): ")

my_key = PublicKey(prompt)
my_key.print_public_keys()
my_key.print_private_keys()
for i in range(11, 16):
    my_key.private_key = hex(i)
    my_key.print_public_keys()
    my_key.print_private_keys()
