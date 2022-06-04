#digsig.py
from ecdsa import SigningKey, SECP256k1, VerifyingKey
from ecdsa.util import randrange_from_seed__trytryagain

DEFAULT_CURVE = SECP256k1
def sk_from_seed(seed, curve):
	secexp = randrange_from_seed__trytryagain(seed, curve.order)
	return SigningKey.from_secret_exponent(secexp, curve=curve)

def sign(sk, msg):
	return sk.sign(msg)

def check(pk, sig, msg):
	return pk.verify(sig, msg)
