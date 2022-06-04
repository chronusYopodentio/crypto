#!/home/playerone/Code/projects/crypto/venv/bin/python3
'''
I haven't yet figured out how to implement a 'transaction'. So I'll be just implement
a chain of blocks contains an abitrary message. 
The blockchain will be stored in sqlite
'''
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import String, Integer
Base = declarative_base()

class Block(Base):
	__tablename__ = "chain01"

	prevHash = Column(String(32), nullable=False)
	thisHash = Column(String(32), primary_key=True)
	nonce = Column(Integer, nullable=False)
	height = Column(Integer, unique=True, nullable=False)
	message = Column(String(256))

	def __repr__(self):
		return f"Block {self.thisHash!r}"


	




