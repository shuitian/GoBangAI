#-*- coding:utf-8 –*-
import sys,pygame,time
sys.path.append("..")
import system.sql
class game(object):
	"""游戏类"""
	def __init__(self, window):
		"""初始化窗口和玩家"""
		super(game, self).__init__()
		self.window = window
		self.black = None
		self.white = None
		self.in_progress = False
		self.winner = None
		self.round = 0
		self.startTime = None
		self.endTime = None
		self.game_box = None

	def start_game(self):
		"""开始游戏"""
		if not self.in_progress:
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
		"""下一回合"""
		self.round = self.round + 1
