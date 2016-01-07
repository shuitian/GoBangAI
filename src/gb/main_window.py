#-*- coding:utf-8 –*-
import pygame
from pygame.locals import *
import os,sys
sys.path.append("..")
import system.events,system.sql,system.file_path
import gbgui.buttons

class MainWindow(object):
	"""主窗口类"""
	def __init__(self, width = 1366, height = 768):
		"""初始化窗口大小，标题等"""
		super(MainWindow, self).__init__()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
		pygame.display.set_caption(u"五子棋".encode('utf-8'))
		
		self.sql = system.sql.sql()
		self.player = self.sql.get_last_player()
		self.buttons = []
		
	
	def set_game(self, game):
		"""设置当前游戏变量"""
		self.current_game = game

	def handle_event(self):
		"""处理事件信息"""
		for event in pygame.event.get():
			if event.type == QUIT:
				# del self.sql
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				system.events.press_mouse_button_down(self, event)

	def add_none_click_button(self, button, position):
		"""在屏幕上添加一个无点击事件按钮"""
		button.render(self.screen, position)

	def add_button(self, button, position):
		"""在屏幕上添加一个有点击事件按钮"""
		self.add_none_click_button(button, position)
		self.buttons.append(button)

	def clear_button(self):
		"""屏幕上的所有按钮不再响应事件"""
		self.button = []

	def set_background(self, background_image_filename = system.file_path.get_res_path('background.png')):
		"""设置窗口背景"""
		self.clear_button()
		background = pygame.image.load(background_image_filename).convert()	
		self.screen.blit(background, (0,0))

	def add_start_and_exit_button(self):
		"""添加开始和结束按钮"""
		start_button = gbgui.buttons.text_button(name = "start", text = u"开始游戏", click = system.events.press_start_button)
		self.add_button(start_button, (self.width/2 - start_button.rect.width/2, self.height/4*3 - start_button.rect.height/2))
		exit_button = gbgui.buttons.text_button(name = "exit", text = u"退出游戏", click = system.events.press_exit_button)
		self.add_button(exit_button, (self.width/2 - start_button.rect.width/2, self.height/6*5 - start_button.rect.height/2))
	def display_player_name(self):
		"""显示玩家姓名"""
		player_name = gbgui.buttons.text_button(name = "player_name", text =self.player, click = None)
		self.add_none_click_button(player_name, (self.width/2 + 6*player_name.rect.width, self.height/4*3 - player_name.rect.height/2))
	def change_player_name(self):
		"""修改玩家姓名"""
		new_player_name = gbgui.buttons.text_button(name = "new_player_name", text =u"修改玩家姓名", click = self.sql.set_last_player(self.player))
		self.add_button(new_player_name, (self.width/2 + 2*new_player_name.rect.width, self.height/6*5 - new_player_name.rect.height/2))
	def main_loop(self):
		"""主循环"""
		self.set_background()
		self.add_start_and_exit_button()
		self.display_player_name()
		self.change_player_name()
		while True:
			self.handle_event()	
			pygame.display.update()

if __name__ == '__main__':
	"""实例化主窗口，并开始主循环"""
	pygame.init()
	window = MainWindow()
	window.main_loop()
