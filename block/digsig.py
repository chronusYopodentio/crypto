#digsig.py
from ecdsa import SigningKey, SECP256k1, VerifyingKey
import random
from binascii import hexlify
from ecdsa.util import randrange_from_seed__trytryagain

'''
random.seed(123)
sk = bytes([random.randint(0,255) for i in range(32)])
sk_string = 
'''
CURVE = SECP256k1
SEED = 1337
def makeKey(seed, curve):
	secexp = randrange_from_seed__trytryagain(seed, curve.order)
	return SigningKey.from_secret_exponent(secexp, curve=curve)

sk = makeKey(SEED, CURVE)
sk_string = hexlify(makeKey(SEED, CURVE).to_string()).decode()

vk = sk.verifying_key

signature = sk.sign(b"test")
assert vk.verify(signature, b"test")

print("error less")


		
	

		

