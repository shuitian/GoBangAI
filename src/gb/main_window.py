#-*- coding:utf-8 –*-
import pygame
from pygame.locals import *
import os,sys
sys.path.append("..")
import system.file_path
import system.events
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
		
		self.buttons = []
	
	def handle_event(self):
		"""处理事件信息"""
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				system.events.press_mouse_button_down(self, event)

	def add_button(self, button, position):
		"""在屏幕上添加一个按钮"""
		self.buttons.append(button)
		button.render(self.screen, position)

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
		exit_button = gbgui.buttons.text_button(name = "start", text = u"退出游戏", click = system.events.press_exit_button)
		self.add_button(exit_button, (self.width/2 - start_button.rect.width/2, self.height/6*5 - start_button.rect.height/2))

	def main_loop(self):
		"""主循环"""
		self.set_background()
		self.add_start_and_exit_button()
		while True:
			self.handle_event()	
			pygame.display.update()

if __name__ == '__main__':
	"""实例化主窗口，并开始主循环"""
	pygame.init()
	window = MainWindow()
	window.main_loop()
