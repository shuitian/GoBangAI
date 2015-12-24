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
	def __init__(self, width=640, height=480):
		"""初始化窗口大小，标题等"""
		super(MainWindow, self).__init__()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption("GoBang!")
		
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

	def set_background(self, background_image_filename):
		"""设置窗口背景"""
		background = pygame.image.load(background_image_filename).convert()	
		self.screen.blit(background, (0,0))
		start_button = gbgui.buttons.image_button("leaf.png")
		self.add_button(start_button, (0,0))

	def main_loop(self):
		"""主循环"""
		self.set_background(system.file_path.get_res_path('background.jpg'))
		while True:
			self.handle_event()	
			pygame.display.update()

if __name__ == '__main__':
	"""实例化主窗口，并开始主循环"""
	pygame.init()
	window = MainWindow()
	window.main_loop()
