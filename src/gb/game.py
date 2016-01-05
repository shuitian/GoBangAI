#-*- coding:utf-8 –*-
import sys,pygame,time
sys.path.append("..")
import system.sql
class game(object):
	"""游戏类"""
	def __init__(self, window, player1, player2):
		"""初始化窗口和玩家"""
		super(game, self).__init__()
		self.window = window
		self.black = player1
		self.white = player2
		self.in_progress = False
		self.winner = None
		self.round = 0
		self.startTime = None
		self.endTime = None

	def start_game(self):
		"""开始游戏"""
		if not self.in_progress:
			print 1
			self.in_progress = True
			self.startTime = time.time()

	def end_game(self, winner):
		"""结束游戏"""
		if self.in_progress:
			self.in_progress = False
			self.endTime = time.time()
			self.winner = winner
			self.window.sql.insert_game(self)
			# self.window.sql.show_table("GAME")

	def next_round(self):
		self.round = self.round + 1
