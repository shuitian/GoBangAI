#-*- coding:utf-8 –*-
import sqlite3,os
class sql(object):
	"""处理数据库的类"""
	def __init__(self):
		super(sql, self).__init__()
		self.conn = self.create_table()
		
	def __del__(self):
		# super(sql, self).__del__()
		print "close connection"
		self.conn.close()

	def create_table(self):
		if os.path.exists("gobang.db"):
			conn = sqlite3.connect('gobang.db')
		else:
			conn = sqlite3.connect('gobang.db')

			print "Open Success"

			conn.execute('''CREATE TABLE PLAYER(
				name TEXT PRIMARY KEY   NOT NULL,
				ai            INT       NOT NULL
			);''')

			conn.execute('''CREATE TABLE GAME(
				id INT PRIMARY KEY NOT NULL,
				startTime TEXT,
				endTime TEXT,
				blackName TEXT NOT NULL,
				whiteName TEXT NOT NULL,
				winner TEXT NOT NULL,
				round INT
			);''')
		return conn

	def has_name(self, name):
		flag = self.execute("SELECT * from PLAYER WHERE name = "+name)
		for x in flag:
			return True
		return False
		

	def show_table(self, table_name):
		table = self.execute("SELECT *  from " + table_name)
		if table != None:
			for x in table:
				print x

	def insert_name(self, name, ai):
		if self.has_name(name):
			print "Error: name is not unique!"
			return 
		if ai:
			ai = "1"
		else :
			ai = "0"
		self.execute("""INSERT INTO PLAYER (NAME,AI) VALUES(""" + name + "," + ai + ")"
			)
		self.conn.commit()

	def is_ai(self, name):
		table = self.execute("SELECT name, ai from PLAYER WHERE name = "+name)
		if table == None:
			return False
		else:
			for x in table:
				if x[1] == 1:
					return True
				else:
					return False

	def execute(self, seq):
		# print seq
		return self.conn.execute(seq)

	def insert_game(self, game):
		pass

if __name__ == '__main__':
	s = sql()
	s.insert_name("123", ai=True)
	print s.has_name("123")
	print s.is_ai("123")
	s.show_table("PLAYER")
	