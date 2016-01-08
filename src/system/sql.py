#-*- coding:utf-8 –*-
import sqlite3,os,time
import file_path
class sql(object):
	"""处理数据库的类"""
	def __init__(self):
		"""获取数据库连接"""
		super(sql, self).__init__()
		self.create_table()
		# print "create_table"
		
	def __del__(self):
		"""关闭数据库连接"""
		# super(sql, self).__del__()
		# print "close connection"
		self.conn.close()

	def create_table(self):
		"""如果数据库存在，则创建数据库并创建数据表，反之连接数据库"""
		db = file_path.get_res_path('gobang.db')
		if os.path.exists(db):
			self.conn = sqlite3.connect(db)
		else:
			self.conn = sqlite3.connect(db)

			print "Open Success"

			self.conn.execute('''CREATE TABLE PLAYER(
				name TEXT PRIMARY KEY   NOT NULL,
				ai            TEXT      NOT NULL,
				last	TEXT
			);''')

			self.conn.execute('''CREATE TABLE GAME(
				id INTEGER PRIMARY KEY,
				startTime TEXT,
				endTime TEXT,
				blackName TEXT NOT NULL,
				whiteName TEXT NOT NULL,
				winner TEXT NOT NULL,
				round INT
			);''')
			self.insert_name("None", True)

	def has_name(self, name):
		"""PLAYER表中是否有指定名字"""
		flag = self.execute("SELECT * from PLAYER WHERE name = " +  "'" + name + "'")
		for x in flag:
			return True
		return False
		
	def show_table(self, table_name):
		"""显示表中所有数据"""
		table = self.execute("SELECT *  from " + table_name)
		if table != None:
			print table.fetchall()

	def insert_name(self, name, ai):
		"""在PLAYER表中插入数据"""
		if name == "":
			name = None
		if self.has_name(name):
			print "Error: name ('" + name + "') is not unique! Insert failed!"
			return 
		self.execute("""INSERT INTO PLAYER (NAME,AI) \
			VALUES(""" + "'" + name + "'" + ","+ "'" +str(ai) + "'" +")"
			)
		self.conn.commit()

	def is_ai(self, name):
		"""该玩家是否是AI"""
		table = self.execute("SELECT * from PLAYER WHERE name = " +  "'" + name + "'")
		if table == None:
			return False
		else:
			x = table.fetchone()
			return x[1] == "True"

	def execute(self, seq):
		"""执行数据库语句"""
		# print seq
		return self.conn.execute(seq)

	def insert_game(self, game):
		"""在GAME表中插入一条数据"""
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
		"""根据game数据的详情在GAME表中插入一条数据"""
		self.execute("""INSERT INTO GAME (id,startTime,endTime,blackName,whiteName,winner,round) \
			VALUES(null,""" + "'" + startTime + "'" + ","
				+ "'" + endTime + "'" + "," 
					+ "'" + blackName + "'" + ","
						+ "'" + whiteName + "'" + ","
							+ "'" + winner + "'" + ","
								+ str(round) + ")"
			)
		self.conn.commit()

	def get_nr_victories(self, name):
		"""获取该玩家的胜利场次"""
		table = self.execute("SELECT * from GAME WHERE winner = " +  "'" + name + "'")
		return len(table.fetchall())

	def get_nr_games(self, name):
		"""获取该玩家的总游戏场次"""
		table = self.execute("SELECT * from GAME WHERE blackName = " +  "'" + name + "'" + " or whiteName = " +  "'" + name + "'")
		return len(table.fetchall())

	def get_rate_victories(self, name):
		"""获取该玩家的胜率"""
		return ((float)(self.get_nr_victories(name)))/self.get_nr_games(name)

	def get_black_rate_victories(self, name):
		"""获取该玩家的先手胜率"""
		table1 = self.execute("SELECT * from GAME WHERE blackName = " +  "'" + name + "'").fetchall()
		table2 = self.execute("SELECT * from GAME WHERE blackName = " +  "'" + name + "'" + " and winner = " +  "'" + name + "'").fetchall()
		if len(table1) != 0:
			return ((float)(len(table2)))/len(table1)
		return None

	def get_white_rate_victories(self, name):
		"""获取该玩家的后手胜率"""
		table1 = self.execute("SELECT * from GAME WHERE whiteName = " +  "'" + name + "'").fetchall()
		table2 = self.execute("SELECT * from GAME WHERE whiteName = " +  "'" + name + "'" + " and winner = " +  "'" + name + "'").fetchall()
		if len(table1) != 0:
			return ((float)(len(table2)))/len(table1)
		return None

	def get_last_player(self):
		"""获取最新玩家的名字"""
		table = self.execute("SELECT * from PLAYER WHERE last IS NOT NULL").fetchone()
		if table == None:
			return "None"
		return table[0]

	def set_last_player(self, name):
		"""设置最新玩家的名字"""
		table = self.execute("SELECT * from PLAYER WHERE name = " +  "'" + name + "'").fetchone()
		if table == None:
			self.insert_name(name, False)
		self.execute("UPDATE PLAYER SET last = NULL")
		self.execute("UPDATE PLAYER SET last = 'last' WHERE name = " +  "'" + name + "'")
		self.conn.commit()

if __name__ == '__main__':
	"""测试代码"""
	s = sql()
	s.insert_name("black", ai=True)
	s.insert_name("white", ai=False)
	print "是否有black:",s.has_name("black")
	print "black是否是ai:",s.is_ai("black")
	print "white是否是ai:",s.is_ai("white")
	print "最后一次游戏玩家:",s.get_last_player()
	s.set_last_player("black")
	s.show_table("PLAYER")
	print "最后一次游戏玩家:",s.get_last_player()
	s.set_last_player("white1")
	s.show_table("PLAYER")
	print "最后一次游戏玩家:",s.get_last_player()
	import sys
	sys.path.append("..")
	import gb.game,player
	black = player.player("black", False)
	white = player.player("white", True)
	g = gb.game.game(None, white,black )
	g.winner = black
	s.insert_game(g)
	s.show_table("GAME")
	print "black胜利场次:",s.get_nr_victories("black")
	print "white胜利场次:",s.get_nr_victories("white")
	print "black游戏场次:",s.get_nr_games("black")
	print "white游戏场次:",s.get_nr_games("white")
	print "black胜率:",s.get_rate_victories("black")
	print "white胜率:",s.get_rate_victories("white")
	print "black先手胜率:",s.get_black_rate_victories("black")
	print "white先手胜率:",s.get_black_rate_victories("white")
	print "black后手胜率:",s.get_white_rate_victories("black")
	print "white后手胜率:",s.get_white_rate_victories("white")
	print s.get_last_player()