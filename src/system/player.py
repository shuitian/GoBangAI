#-*- coding:utf-8 –*-
import sys,pygame
class player(object):
	"""玩家类"""
	def __init__(self, name, ai):
		super(player, self).__init__()
		self.name = name
		self.ai = ai
