#-*- coding:utf-8 –*-
import sys,pygame
class game(object):
	"""游戏类"""
	def __init__(self, window, player1, player2):
		"""初始化窗口和玩家"""
		super(game, self).__init__()
		self.window = window
		self.black = player1
		self.white = player2
		self.in_progress = False

	def start_game(self):
		"""开始游戏"""
		self.window.current_game = self
		self.in_progress = True

	def end_game(self, winner):
		"""结束游戏"""
		self.in_progress = False

