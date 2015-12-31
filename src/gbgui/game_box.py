#-*- coding:utf-8 –*-
import sys,pygame
sys.path.append("..")
import system.file_path
import gb.main_window
class game_box(object):
	"""游戏棋盘类"""
	def __init__(self, window, size = 700, nr_lines = 13):
		"""初始化棋盘大小"""
		super(game_box, self).__init__()
		self.window = window
		self.size = size
		self.nr_lines = nr_lines
		self.space = self.size/(self.nr_lines+1)

	def draw_box(self):
		"""在屏幕上绘制棋盘"""
		self.draw_lines()
		self.draw_points()

	def draw_lines(self):
		"""画线"""
		line_color = (0,0,0)
		line_width = 2
		for x in xrange(1,self.nr_lines+1):
			start_pot = ((self.window.width-self.size)/2,(self.window.height-self.size)/2 + x*self.space)
			end_pot = ((self.window.width+self.size)/2,(self.window.height-self.size)/2 + x*self.space)
			pygame.draw.line(self.window.screen, line_color, start_pot, end_pot, line_width)

			start_pot = ((self.window.width-self.size)/2 + x*self.space,(self.window.height-self.size)/2)
			end_pot = ((self.window.width-self.size)/2 + x*self.space,(self.window.height+self.size)/2)
			pygame.draw.line(self.window.screen, line_color, start_pot, end_pot, line_width)
		"""画边框"""
		edge_color = (150,118,75)
		edge_width = 10
		pygame.draw.rect(self.window.screen, edge_color, ((self.window.width-self.size)/2,(self.window.height-self.size)/2,self.size,self.size), edge_width)

	def draw_points(self):
		"""画点"""
		radius = 5
 		points = []
		points.append(self.get_screen_position_from_game_point(((self.nr_lines+3)/2-1,(self.nr_lines+3)/2-1)))
		points.append(self.get_screen_position_from_game_point(((self.nr_lines+3)/4-1,(self.nr_lines+3)/4-1)))
		points.append(self.get_screen_position_from_game_point(((self.nr_lines+3)/4-1,(self.nr_lines+3)/4*3-1)))
		points.append(self.get_screen_position_from_game_point(((self.nr_lines+3)/4*3-1,(self.nr_lines+3)/4-1)))
		points.append(self.get_screen_position_from_game_point(((self.nr_lines+3)/4*3-1,(self.nr_lines+3)/4*3-1)))
		for point in points:
			pygame.draw.circle(self.window.screen,[0,0,0],point,radius,0)

		"""for test"""
		# p = system.file_path.get_res_path('white_point.png')
		# background = pygame.image.load(p).convert_alpha()
		# self.window.screen.blit(background, [points[0][0]-18,points[0][1]-18])

	def get_screen_position_from_game_point(self, place):
		"""根据棋盘点位置获取屏幕点位置"""
		start_pot = ((self.window.width-self.size)/2,(self.window.height-self.size)/2)
		x = self.space * place[0] + start_pot[0]
		y = self.space * place[1] + start_pot[1]
		return [x+1,y+1]


if __name__ == '__main__':
	"""实例化主窗口"""
	pygame.init()
	window = gb.main_window.MainWindow()
	window.main_loop()