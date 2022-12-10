import base58  # pip install base58

# these modules are taken from here https://github.com/karpathy/cryptos/tree/main/cryptos
from ripemd160 import ripemd160
from sha256 import sha256


class PublicKey:

    """Calculating public key from private key"""
    """Parameters of an elliptic curve"""
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
        try:
            private_key = int(private_key, 16)
        except ValueError:
            raise NotImplementedError(
                'Private key must be a hexadecimal number')
        if private_key <= 0 or private_key >= self.n_curve:
            raise Exception("Invalid Scalar/Private Key")
        self.__private_key = private_key

    def __modinv(self, a, n):
        """Extended Euclidean Algorithm"""

        lm, hm = 1, 0
        low, high = a % n, n
        while low > 1:
            ratio = int(high/low)
            nm, new = int(hm-lm*ratio), int(high-low*ratio)
            lm, low, hm, high = nm, new, lm, low
        return lm % n

    def __ec_add(self, a, b):
        """Point addition"""

        lam_add = ((b[1]-a[1]) * self.__modinv(b[0] -
                   a[0], self.p_curve)) % self.p_curve
        x = (pow(lam_add, 2)-a[0]-b[0]) % self.p_curve
        y = (lam_add*(a[0]-x)-a[1]) % self.p_curve
        return x, y

    def __ec_double(self, a):
        """EC point doubling"""

        lam = ((3*a[0]*a[0]+self.a_curve) *
               self.__modinv((2*a[1]), self.p_curve)) % self.p_curve
        x = int((lam*lam-2*a[0]) % self.p_curve)
        y = int((lam*(a[0]-x)-a[1]) % self.p_curve)
        return x, y

    def __ec_multiply(self, genpoint, scalarhex):
        """EC point multiplication"""
        scalarbin = str(bin(scalarhex))[2:]
        q = genpoint
        for i in range(1, len(scalarbin)):  # Double and add to multiply point
            q = self.__ec_double(q)
            if scalarbin[i] == "1":
                q = self.__ec_add(q, genpoint)
        return q

    def __compute_public(self):
        """Calculating a public key"""
        return self.__ec_multiply(self.gpoint, self.__private_key)

    def __public_address(self, key):
        """Function calculating address"""
        # bytes representation is needed for sha256 and ripemd160
        key = bytes.fromhex(key)
        address = bytes.fromhex(f"00{ripemd160(sha256(key)).hex()}")
        checksum = sha256(sha256(address))
        address = f"{address.hex()}{checksum.hex()[:8]}"
        address = base58.b58encode(bytes.fromhex(address)).decode("UTF-8")
        return address

    def __convert_private_to_wif(self):
        """Converting a private key to WIF"""

        # convert private key to bytes for sha256
        private_wif = bytes.fromhex(f"80{hex(self.__private_key)[2:]:0>64}")
        private_wif_comp = bytes.fromhex(
            f"80{hex(self.__private_key)[2:]:0>64}01")

        checksum = sha256(sha256(private_wif))
        checksum_comp = sha256(sha256(private_wif_comp))

        private_wif = f"{private_wif.hex()}{checksum.hex()[:8]}"
        private_wif_comp = f"{private_wif_comp.hex()}{checksum_comp.hex()[:8]}"

        private_wif = base58.b58encode(
            bytes.fromhex(private_wif)).decode("UTF-8")
        private_wif_comp = base58.b58encode(
            bytes.fromhex(private_wif_comp)).decode("UTF-8")

        return private_wif, private_wif_comp

    def print_private_keys_wif(self):
        """Printing private keys in WIF"""
        priv_key, priv_key_comp = self.__convert_private_to_wif()
        print(f"\nWIF - private key\n{priv_key}")
        print(f"Length: {len(priv_key)}\n")
        print(f"WIF compressed - private key\n{priv_key_comp}")
        print(f"Length: {len(priv_key_comp)}\n")

    def print_public_key(self):
        """Printing public key in different formats"""
        public_key = self.__compute_public()
        print("\nThe uncompressed public key (not address):")
        print(public_key)
        print("\nThe uncompressed public key (HEX):")
        uncomp_pub = f"04{(hex(public_key[0])[2:]):0>64}{(hex(public_key[1])[2:]):0>64}"
        print(uncomp_pub)
        print(f"Length: {len(uncomp_pub)}\n")
        uncomp_addr = self.__public_address(uncomp_pub)
        print(f"Address from uncompressed key\n{uncomp_addr}")
        print("\nThe official Public Key - compressed:")
        if public_key[1] % 2 == 1:  # If the Y value for the Public Key is odd.
            comp_pub = f"03{hex(public_key[0])[2:]:0>64}"
            print(comp_pub)
            print(f"Length: {len(comp_pub)}\n")
            comp_addr = self.__public_address(comp_pub)
            print(f"Address from compressed key\n{comp_addr}")
        else:  # Or else, if the Y value is even.
            comp_pub = f"02{hex(public_key[0])[2:]:0>64}"
            print(comp_pub)
            print(f"Length: {len(comp_pub)}\n")
            comp_addr = self.__public_address(comp_pub)
            print(f"Address from compressed key\n{comp_addr}")


prompt = input(f"Please insert your private key in HEX format (0x): ")

my_key = PublicKey(prompt)
my_key.print_public_key()
my_key.print_private_keys_wif()
