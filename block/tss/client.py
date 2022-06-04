#tss client side
import socket, struct
from Crypto.Hash import RIPEMD160 as rip
from hashlib import sha256
from ecdsa import VerifyingKey
from datetime import datetime
from sign import sk_from_seed, sign, check, DEFAULT_CURVE

SEED = 1234 
MSG = "message to time-stamp"

sk = sk_from_seed(1337, DEFAULT_CURVE)
pk = sk.verifying_key
h = rip.new()
h.update(pk.to_string())
addr = h.digest()

sh = sha256()
sh.update(MSG.encode())
y = sh.digest()

def client(sock, host, port, msg):
	sock.connect((host,port))
	sock.sendall(msg)
	sc = sock.recv(136)
	server_pk = sc[0:64]
	timestamp = sc[64:72]
	sc = sc[72:]
	toCheck = msg + timestamp
	server_pk = VerifyingKey.from_string(server_pk, DEFAULT_CURVE)
	timestamp = struct.unpack('d', timestamp)[0]
	msg = check(server_pk, sc, toCheck)
	print("timestamp recv: ", timestamp)
	print("msg: ", msg)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	host = "127.0.0.1"
	port = 8000
	msg = addr + y
	client(sock, host, port, msg)
