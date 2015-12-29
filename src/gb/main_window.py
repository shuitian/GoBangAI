#-*- coding:utf-8 –*-
import pygame
from pygame.locals import *
import os,sys
sys.path.append("..")
import system.file_path
import system.events
import gbgui.buttons
from win32api import GetSystemMetrics

class MainWindow(object):
	"""主窗口类"""
	def __init__(self):
		"""初始化窗口大小，标题等"""
		super(MainWindow, self).__init__()
		self.width = GetSystemMetrics (0)
		self.height = GetSystemMetrics (1)
		self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN, 32)
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
		self.button = []

	def set_background(self, background_image_filename):
		"""设置窗口背景"""
		background = pygame.image.load(background_image_filename).convert()	
		self.screen.fill((255,255,255))
		self.screen.blit(background, (0,0))
		start_button = gbgui.buttons.text_button(name = "start", text = u"开始游戏", click = system.events.press_start_button)
		self.add_button(start_button, (self.width/2 - start_button.rect.width/2, self.height/4*3 - start_button.rect.height/2))
		exit_button = gbgui.buttons.text_button(name = "start", text = u"退出游戏", click = system.events.press_exit_button)
		self.add_button(exit_button, (self.width/2 - start_button.rect.width/2, self.height/5*4 - start_button.rect.height/2))

	def main_loop(self):
		"""主循环"""
		self.set_background(system.file_path.get_res_path('background.png'))
		while True:
			self.handle_event()	
			pygame.display.update()

if __name__ == '__main__':
	"""实例化主窗口，并开始主循环"""
	pygame.init()
	print "width =", GetSystemMetrics (0)
	print "height =",GetSystemMetrics (1)
	window = MainWindow()
	window.main_loop()
