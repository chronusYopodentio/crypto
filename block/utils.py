from binascii import hexlify
class Utils:
	def b2s(self, b: bytes) -> str:
		return hexlify(b).decode()
		
