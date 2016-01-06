#-*- coding:utf-8 –*-
import sys,pygame
sys.path.append("..")
import system.file_path
class my_button(pygame.sprite.Sprite):
	"""按钮的基类"""
	def __init__(self, name, click = None):
		super(my_button, self).__init__()
		self.name = name
		self.on_click = click
		self.image = None
		self.rect = None

	def render(self, surface, topleft):
		"""渲染"""
		self.rect.topleft = topleft
		if self.image:
			surface.blit(self.image,self.rect)

	def is_over(self, point):
		"""如果point在自身范围内，返回True"""
		return self.rect.collidepoint(point)

class image_button(my_button):
	"""以图片为背景的按钮"""
	def __init__(self, name, image_filename, click = None):
		super(image_button, self).__init__(name, click)
		self.image = pygame.image.load(system.file_path.get_res_path(image_filename)).convert_alpha()
		self.rect = self.image.get_rect()

class text_button(my_button):
	"""以文字为背景的按钮"""
	def __init__(self, name, text, size = 30, font = system.file_path.get_res_path("STXINGKA.TTF"), color = (0,0,0), click = None):
		super(text_button, self).__init__(name, click)
		my_font = pygame.font.Font(font, size)
		self.image = my_font.render(text, True, color)
		self.rect = self.image.get_rect()