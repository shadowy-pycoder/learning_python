# Super simple Elliptic Curve Presentation. No imported>
# For educational purposes only. Remember to use Python>

# Below are the public specs for Bitcoin's curve - the >

Pcurve = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2>
N=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD>
Acurve = 0; Bcurve = 7 # These two defines the elliptic>
Gx = 55066263022277343669578718895168534326250603453777>
Gy = 32670510020758816978083085130507043184471273380659>
GPoint = (Gx,Gy) # This is our generator point. Trillio>

#Individual Transaction/Personal Information
privKey = 0xCC4845C9779B08D4EDBAEBA9BC926DDF347803CCDD8>

def modinv(a,n=Pcurve): #Extended Euclidean Algorithm/'>
    lm, hm = 1,0
    low, high = a%n,n
    while low > 1:
        ratio = int(high/low)
        nm, new = int(hm-lm*ratio), int(high-low*ratio)
        lm, low, hm, high = nm, new, lm, low
    return lm % n

def ECadd(a,b): # Not true addition, invented for EC. C>
    LamAdd = ((b[1]-a[1]) * modinv(b[0]-a[0],Pcurve)) %>
    x = (LamAdd*LamAdd-a[0]-b[0]) % Pcurve
    y = (LamAdd*(a[0]-x)-a[1]) % Pcurve
    return (x,y)

def ECdouble(a): # This is called point doubling, also >
    Lam = ((3*a[0]*a[0]+Acurve) * modinv((2*a[1]),Pcurv>
    x = int((Lam*Lam-2*a[0]) % Pcurve)
    y = int((Lam*(a[0]-x)-a[1]) % Pcurve)
    return (x,y)

def EccMultiply(GenPoint,ScalarHex): #Double & add. Not>
    if ScalarHex == 0 or ScalarHex >= N: raise Exceptio>
    ScalarBin = str(bin(ScalarHex))[2:]
    Q=GenPoint
    for i in range (1, len(ScalarBin)): # This is inven>
        Q=ECdouble(Q) # print "DUB", Q[0]; print
        if ScalarBin[i] == "1":
            Q=ECadd(Q,GenPoint) # print "ADD", Q[0]; pr>
    return (Q)
#ScalarBin = str(bin(privKey))[2:]
#print(f"ScalarBin: {ScalarBin} \nScalarBin len: {len(S>
#print(f"Pcurve: {Pcurve}")
print("******* Public Key Generation *********")
PublicKey = EccMultiply(GPoint,privKey)
#Add = ECadd(GPoint,GPoint)
#Double = ECdouble(GPoint)
#print(f"Addition: {Add} \nDoubling: {Double}")
print("the private key:")
print(f"{privKey}")
print("\nthe uncompressed public key (not address):")
print(f"{PublicKey}")
print("\nthe uncompressed public key (HEX):")
message = f"04{(hex(PublicKey[0])[2:]):064}{(hex(Public>
print(message.upper())
print(f"Length: {len(message)}")
print("\nthe official Public Key - compressed:")
if PublicKey[1] % 2 == 1: # If the Y value for the Publ>
    print(f"03{hex(PublicKey[0])[2:]:064}")
else: # Or else, if the Y value is even.
    print(f"02{hex(PublicKey[0])[2:]:064}")
