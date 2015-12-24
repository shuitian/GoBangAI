#-*- coding:utf-8 –*-
import sys,pygame
sys.path.append("..")
import system.file_path
class my_button(pygame.sprite.Sprite):
	"""按钮的基类"""
	def __init__(self, name):
		super(my_button, self).__init__()
		self.name = name

	def render(self, surface, topleft):
		"""渲染"""
		self.rect.topleft = topleft
		surface.blit(self.image,self.rect)

	def is_over(self, point):
		"""如果point在自身范围内，返回True"""
		return self.rect.collidepoint(point)

class image_button(my_button):
	"""以图片为背景的按钮"""
	def __init__(self, name, image_filename):
		super(image_button, self).__init__(name)
		self.image = pygame.image.load(system.file_path.get_res_path(image_filename))
		self.rect = self.image.get_rect()

class text_button(my_button):
	"""以文字为背景的按钮"""
	def __init__(self, name, text, size = 30, font = "宋体", color = (0,0,0)):
		super(text_button, self).__init__(name)
		my_font = pygame.font.SysFont(font, size)
		self.image = my_font.render(text, True, color)
		self.rect = self.image.get_rect()

		