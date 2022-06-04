import struct
class Transaction:
	def __init__(self, src, des, value, sig):
		if not isinstance(src, bytes) and len(src) != 20:
			raise TypeError
		if not isinstance(des, bytes) and len(des) != 20:
			raise TypeError
		if not isinstance(value, int):
			raise TypeError
		if not isinstance(sig, bytes):
			raise TypeError

		self.src = src
		self.des = des
		self.value = value
		self.sig = sig
				
	@property
	def value(self):
		return self.val

	@value.setter
	def value(self, val):
		self.val = struct.pack('i', val)
	
	
	sig = None



