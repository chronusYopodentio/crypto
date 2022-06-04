#time-stamp server
import socket, struct
from datetime import datetime
from sign import sk_from_seed, sign, DEFAULT_CURVE

class Server:
	sock = None
	def __init__(self, host, port, seed):
		self.host = host
		self.port = port
		self.seed = seed
		self.sk = sk_from_seed(self.seed, DEFAULT_CURVE)
		self.pk = self.sk.verifying_key


def parse_info(info:bytes):
	addr = info[0:20]
	y = info[20:52]
	return addr, y

def cert(addr, y):
	dt = datetime.now()
	ts = datetime.timestamp(dt)
	print("timestampped: ", ts)
	t = struct.pack('d', ts)
	return t, addr + y + t

def main(server):
	sock = server.sock
	host = server.host
	port = server.port
	sock.bind((host, port))
	sock.listen()
	conn, addr = sock.accept()
	with conn:
		print(f"connected by {addr}")
		while True:
			info = conn.recv(52)
			if not info:
				print(f"connection closed: {addr}")
				break

			addr, y = parse_info(info)
			t, c = cert(addr, y)
			sc = sign(server.sk, c)
			conn.sendall(server.pk.to_string() + t + sc)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	if __name__ == "__main__":
		host = "127.0.0.1"
		port = 8000
		seed = 1337
		server = Server(host, port, seed)
		server.sock = sock
		main(server)
