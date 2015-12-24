#-*- coding:utf-8 –*-
import sys,pygame
sys.path.append("..")
import system.file_path
class image_button(pygame.sprite.Sprite):
	"""以图片为背景的按钮"""
	def __init__(self, image_filename):
		super(image_button, self).__init__()
		self.image = pygame.image.load(system.file_path.get_res_path(image_filename))
		self.rect = self.image.get_rect()

	def render(self, surface, topleft):
		"""渲染"""
		self.rect.topleft = topleft
		surface.blit(self.image,self.rect)

	def is_over(self, point):
		"""如果point在自身范围内，返回True"""
		return self.rect.collidepoint(point)