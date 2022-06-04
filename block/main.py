#!/home/playerone/projects/crypto/venv/bin/python3
from block import Block, Base
import work
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
'''
simple implementation that store blockchain in sql
'''
ENGINE = create_engine("sqlite:///block.db", echo = True, future=True)
SESSION = Session(ENGINE)

def adder(blocks, engine):
	with Session(engine) as session:
		session.add_all(blocks)
		session.commit()


def main(engine, session):
	while True:
		cmd = input('> ')
		cmd = cmd.split(' ')

		if cmd[0]=='exit':
			return 0
		
		elif cmd[0]=='add':
			msg = input('msg: ')
			createBlock(msg)



if __name__=='__main__':
	main(SESSION, ENGINE)	
	
	





