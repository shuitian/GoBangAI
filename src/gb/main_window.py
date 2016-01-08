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
		self.player = self.sql.get_last_player_name()
		self.buttons = []
		self.texts = []
		self.new_name = []
		self.modify = False
		self.current_game = None
	
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
			elif event.type == KEYDOWN and self.modify == True:
				self.append_new_name(event.key)

	def append_new_name(self, key):
		if key == K_BACKSPACE and len(self.new_name)>=1:
			self.new_name = self.new_name[:-1]
		elif len(self.new_name)>=10:
			return
		else:
			alpha_bet = [(x+97)for x in xrange(0,26)]
			if key in alpha_bet:
				self.new_name.append(chr(key))
		self.player = "".join(self.new_name)
		self.new_player_name.text = self.player
		self.add_none_click_button(self.new_player_name, (self.width/4*3 - self.new_player_name.get_rect().width/2, self.height/10*5 - self.new_player_name.get_rect().height/2))

	def show_texts(self):
		self.set_background()
		if self.current_game and self.current_game.game_box:
			self.current_game.game_box.update()
			return 
		for x in self.texts:
			x[0].render(self.screen, x[1])
		for x in self.buttons:
			x[0].render(self.screen, x[1])
				
	def add_none_click_button(self, button, position):
		"""在屏幕上添加一个无点击事件按钮"""
		button.render(self.screen, position)
		for btn in self.texts:
			if button.name == btn[0].name:
				self.texts.remove(btn)
				break
		self.texts.append([button, position])

	def add_button(self, button, position):
		"""在屏幕上添加一个有点击事件按钮"""
		button.render(self.screen, position)
		for btn in self.buttons:
			if button.name == btn[0].name:
				self.buttons.remove(btn)
				break
		self.buttons.append([button, position])

	def clear_buttons(self):
		"""屏幕上的所有按钮不再响应事件"""
		self.buttons = []
		self.texts = []

	def set_background(self, background_image_filename = system.file_path.get_res_path('background.png')):
		"""设置窗口背景"""
		background = pygame.image.load(background_image_filename).convert()	
		self.screen.blit(background, (0,0))

	def add_start_and_exit_button(self):
		"""添加开始和结束按钮"""
		start_button = gbgui.buttons.text_button(name = "start", text = u"开始游戏", click = system.events.press_start_button)
		self.add_button(start_button, (self.width/2 - start_button.rect.width/2, self.height/10*7 - start_button.rect.height/2))
		exit_button = gbgui.buttons.text_button(name = "exit", text = u"退出游戏", click = system.events.press_exit_button)
		self.add_button(exit_button, (self.width/2 - start_button.rect.width/2, self.height/10*8 - start_button.rect.height/2))

	def display_player_name(self):
		"""显示玩家姓名"""
		self.player = self.sql.get_last_player_name()
		self.player_name = gbgui.buttons.text_button(name = "player_name", text =self.player, click = None)
		self.add_none_click_button(self.player_name, (self.width/4*3 - self.player_name.rect.width/2, self.height/10*7 - self.player_name.rect.height/2))
		self.modify_player_name = gbgui.buttons.text_button(name = "modify_player_name", text =u"修改玩家姓名", click = system.events.press_modify_player_name)
		self.add_button(self.modify_player_name, (self.width/4*3 - self.modify_player_name.rect.width/2, self.height/10*8 - self.modify_player_name.rect.height/2))

	def change_player_name(self):
		"""修改玩家姓名"""
		self.modify = True
		self.new_player_name = gbgui.buttons.edit_text(name = "new_player_name", text = u"请输入您的姓名:")
		self.add_none_click_button(self.new_player_name, (self.width/4*3 - self.new_player_name.rect.width/2, self.height/10*5 - self.new_player_name.rect.height/2))
		self.confirm_button = gbgui.buttons.text_button(name = "confirm_button", text =u"确认修改", click = system.events.press_confirm_change_player_name)
		self.cancel_button = gbgui.buttons.text_button(name = "cancel_button", text =u"取消", click = system.events.press_cancel_change_player_name)
		self.add_button(self.confirm_button, (self.width/4*3 - (self.confirm_button.rect.width + self.cancel_button.rect.width + 50)/2, self.height/10*6 - self.confirm_button.rect.height/2))
		self.add_button(self.cancel_button, (self.width/4*3 - (-self.confirm_button.rect.width + self.cancel_button.rect.width)/2, self.height/10*6 - self.cancel_button.rect.height/2))

	def init(self):
		self.clear_buttons()
		self.set_background()
		self.add_start_and_exit_button()
		self.display_player_name()
		self.new_name = []
		self.modify = False

	def main_loop(self):
		"""主循环"""
		self.init()
		while True:
			self.show_texts()
			self.handle_event()	
			pygame.display.update()

if __name__ == '__main__':
	"""实例化主窗口，并开始主循环"""
	pygame.init()
	window = MainWindow()
	window.main_loop()
