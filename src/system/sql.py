#-*- coding:utf-8 –*-
import sqlite3,os,time
import file_path
class sql(object):
	"""处理数据库的类"""
	def __init__(self):
		super(sql, self).__init__()
		self.conn = self.create_table()
		print "create_table"
		
	def __del__(self):
		# super(sql, self).__del__()
		print "close connection"
		self.conn.close()

	def create_table(self):
		db = file_path.get_res_path('gobang.db')
		if os.path.exists(db):
			conn = sqlite3.connect(db)
		else:
			conn = sqlite3.connect(db)

			print "Open Success"

			conn.execute('''CREATE TABLE PLAYER(
				name TEXT PRIMARY KEY   NOT NULL,
				ai            TEXT      NOT NULL
			);''')

			conn.execute('''CREATE TABLE GAME(
				id INTEGER PRIMARY KEY,
				startTime TEXT,
				endTime TEXT,
				blackName TEXT NOT NULL,
				whiteName TEXT NOT NULL,
				winner TEXT NOT NULL,
				round INT
			);''')
		return conn

	def has_name(self, name):
		flag = self.execute("SELECT name, ai from PLAYER WHERE name = " +  "'" + name + "'")
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
			print "Error: name ('" + name + "') is not unique!"
			return 
		self.execute("""INSERT INTO PLAYER (NAME,AI) VALUES(""" + "'" + name + "'" + "," + "'" +str(ai) + "'" +")"
			)
		self.conn.commit()

	def is_ai(self, name):
		table = self.execute("SELECT name, ai from PLAYER WHERE name = " +  "'" + name + "'")
		if table == None:
			return False
		else:
			for x in table:
				return x[1] == "True"

	def execute(self, seq):
		# print seq
		return self.conn.execute(seq)

	def insert_game(self, game):
		if game == None:
			return
		if game.startTime == None:
			startTime = "None"
		else:
			startTime = time.ctime(game.startTime)
		if game.endTime == None:
			endTime = "None"
		else:
			endTime = time.ctime(game.endTime)
		if game.black == None or game.black.name == None:
			blackName = "None"
		else:
			blackName = game.black.name
		if game.white == None or game.white.name == None:
			whiteName = "None"
		else:
			whiteName = game.white.name
		if game.winner == None or game.winner.name == None:
			winner = "None"
		else:
			winner = game.winner.name
		self.insert_game_detail(startTime, endTime, blackName, whiteName, winner, game.round)

	
	def insert_game_detail(self, startTime, endTime, blackName, whiteName, winner, round):
		self.execute("""INSERT INTO GAME (id,startTime,endTime,blackName,whiteName,winner,round) \
			VALUES(null,""" + "'" + startTime + "'" + ","
				+ "'" + endTime + "'" + "," 
					+ "'" + blackName + "'" + ","
						+ "'" + whiteName + "'" + ","
							+ "'" + winner + "'" + ","
								+ str(round) + ")"
			)
		self.conn.commit()

if __name__ == '__main__':
	s = sql()
	s.insert_name("black", ai=True)
	s.insert_name("white", ai=False)
	print s.has_name("black")
	print s.is_ai("black")
	print s.is_ai("white")
	s.show_table("PLAYER")
	import sys
	sys.path.append("..")
	import gb.game,player
	black = player.player("black", False)
	white = player.player("white", True)
	g = gb.game.game(None, black, white)
	s.insert_game(g)
	s.show_table("GAME")
	