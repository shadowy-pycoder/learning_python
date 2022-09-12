#from hashlib import sha256
import hashlib
import base58
import binascii

class PublicKey:
    """Calculating a public key using private key"""
    def __init__(self, private_key):
        self.private_key = private_key
        self.p_curve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1 # The proven prime
        self.n_curve = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141 # Number of points in the field
        self.a_curve, self.b_curve = 0, 7 # These two defines the elliptic curve. y^2 = x^3 + Acurve * x + Bcurve
        self.gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
        self.gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
        self.gpoint = (self.gx, self.gy) # This is our generator point. Trillions of dif ones possible

    def hash(self, key):
        """Function performing SHA-256 hashing"""
        sha = hashlib.sha256()
        sha.update(binascii.unhexlify(key))
        return sha.hexdigest()

    def public_address(self, key):
        """Function calculating address"""
        ripemd = hashlib.new('ripemd160')
        sha = hashlib.sha256()
        sha.update(binascii.unhexlify(key))
        ripemd.update(sha.digest())
        address = f"00{ripemd.hexdigest()}"
        checksum = self.hash(self.hash(address))[:8]
        address = f"{address}{checksum}"
        address = base58.b58encode(bytes.fromhex(address)).decode("UTF-8")
        return address

    def privatewif(self):
        """Converting a private key to WIF"""

        private_wif = f"80{hex(self.private_key)[2:]}"
        private_wif_comp = f"80{hex(self.private_key)[2:]}01"
        checksum = self.hash(self.hash(private_wif))[:8]
        checksum_comp = self.hash(self.hash(private_wif_comp))[:8]

        private_wif = f"{private_wif}{checksum}"
        private_wif_comp = f"{private_wif_comp}{checksum_comp}"

        private_wif = base58.b58encode(bytes.fromhex(private_wif)).decode("UTF-8")
        private_wif_comp = base58.b58encode(bytes.fromhex(private_wif_comp)).decode("UTF-8")

        print(f"\nWIF - private key\n{private_wif}")
        print(f"Length: {len(private_wif)}\n")
        print(f"WIF compressed - private key\n{private_wif_comp}")
        print(f"Length: {len(private_wif_comp)}\n")

    def modinv(self, a, n): #Extended Euclidean Algorithm/'division' in elliptic curves
        n = self.p_curve
        lm, hm = 1,0
        low, high = a%n, n
        while low > 1:
            ratio = int(high/low)
            nm, new = int(hm-lm*ratio), int(high-low*ratio)
            lm, low, hm, high = nm, new, lm, low
        return lm % n

    def ecc_add(self, a,b): # Not true addition, invented for EC. Could have been called anything.
        lam_add = ((b[1]-a[1]) * self.modinv(b[0]-a[0],self.p_curve)) % self.p_curve
        x = (lam_add*lam_add-a[0]-b[0]) % self.p_curve
        y = (lam_add*(a[0]-x)-a[1]) % self.p_curve
        return (x,y)

    def ecc_double(self, a): # This is called point doubling, also invented for EC.
        lam = ((3*a[0]*a[0]+self.a_curve) * self.modinv((2*a[1]), self.p_curve)) % self.p_curve
        x = int((lam*lam-2*a[0]) % self.p_curve)
        y = int((lam*(a[0]-x)-a[1]) % self.p_curve)
        return (x,y)

    def ecc_multiply(self, genpoint, scalarhex): #Double & add. Not true multiplication
        if scalarhex == 0 or scalarhex >= self.n_curve: raise Exception("Invalid Scalar/Private Key")
        scalarbin = str(bin(scalarhex))[2:]
        q = genpoint
        for i in range (1, len(scalarbin)): # This is invented EC multiplication.
            q = self.ecc_double(q)
            if scalarbin[i] == "1":
                q = self.ecc_add(q, genpoint)
        return(q)

    def public_calc(self):
        """Calculating a public key"""

        public_key = self.ecc_multiply(self.gpoint, self.private_key)
        print("\nthe uncompressed public key (not address):") 
        print(public_key)
        print("\nthe uncompressed public key (HEX):") 
        message = f"04{(hex(public_key[0])[2:]):064}{(hex(public_key[1])[2:]):064}"
        print(message)
        print(f"Length: {len(message)}\n")
        message = self.public_address(message)
        print(f"Address from uncompressed key\n{message}")
        print("\nthe official Public Key - compressed:") 
        if public_key[1] % 2 == 1: # If the Y value for the Public Key is odd.
            message = f"03{hex(public_key[0])[2:]:064}"
            print(message)
            print(f"Length: {len(message)}\n")
        else: # Or else, if the Y value is even.
            message = f"02{hex(public_key[0])[2:]:064}"
            print(message)
            print(f"Length: {len(message)}\n")
            message = self.public_address(message)
            print(f"Address from compressed key\n{message}")

prompt  = input(f"Please insert your private key in HEX format (0x): ")

try:
    prompt = int(prompt, 16)  # interpret the input as a base-16 number, a hexadecimal.
except ValueError:
    print("You did not enter a hexadecimal number!")
my_key = PublicKey(prompt)
my_key.public_calc()
my_key.privatewif()

