import pygame
from pygame.locals import *
import os,sys
sys.path.append("..")
import system.file_path

class MainWindow(object):
	"""docstring for MainWindow"""
	def __init__(self, width=640, height=480):
		super(MainWindow, self).__init__()
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption("GoBang!")
	
	def handle_event(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()	

	def set_background(self, background_image_filename):
		background = pygame.image.load(background_image_filename).convert()	
		self.screen.blit(background, (0,0))

	def main_loop(self):
		while True:
			self.handle_event()	
			self.set_background(os.path.join(system.file_path.get_res_path(), 'background.jpg'))
			pygame.display.update()

# if __name__ == '__main__':
# 	window = MainWindow()
# 	window.main_loop()