#-*- coding:utf-8 –*-
import sys,pygame
sys.path.append("..")
import system.file_path,system.events
import gb.main_window
import gbgui.buttons
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
		self.draw_buttons()

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

	def draw_buttons(self):
		"""绘制按钮"""
		choose_text = gbgui.buttons.text_button(name = "choose_text", text = u"请选择先手后手", click = None)
		self.window.add_none_click_button(choose_text, (self.window.width - (self.window.width - self.size)/4 - choose_text.rect.width/2, self.window.height/10 - choose_text.rect.height/2))

		btn_black_text = gbgui.buttons.text_button(name = "black_text", text = u"先手执黑", click = system.events.press_black_button)
		btn_black_image = gbgui.buttons.image_button("black_image","black.png",system.events.press_black_button)
		self.window.add_button(btn_black_image, (self.window.width - (self.window.width - self.size)/4 - (btn_black_image.rect.width-btn_black_text.rect.width)/2, self.window.height/5 - btn_black_image.rect.height/2))
		self.window.add_button(btn_black_text, (self.window.width - (self.window.width - self.size)/4 - (btn_black_image.rect.width+btn_black_text.rect.width)/2, self.window.height/5 - btn_black_text.rect.height/2))

		btn_white_text = gbgui.buttons.text_button(name = "white_text", text = u"后手执白", click = system.events.press_white_button)
		btn_white_image = gbgui.buttons.image_button("white_image","white.png",system.events.press_white_button)
		self.window.add_button(btn_white_image, (self.window.width - (self.window.width - self.size)/4 - (btn_white_image.rect.width-btn_white_text.rect.width)/2, self.window.height/10*3 - btn_white_image.rect.height/2))
		self.window.add_button(btn_white_text, (self.window.width - (self.window.width - self.size)/4 - (btn_white_image.rect.width+btn_white_text.rect.width)/2, self.window.height/10*3 - btn_white_text.rect.height/2))

		btn_random_text = gbgui.buttons.text_button(name = "random_text", text = u"随机选择", click = system.events.press_random_button)
		self.window.add_button(btn_random_text, (self.window.width - (self.window.width - self.size)/4 - btn_random_text.rect.width/2, self.window.height/5*2 - btn_random_text.rect.height/2))
	
		btn_return_text = gbgui.buttons.text_button(name = "return_text", text = u"返回主菜单", click = system.events.press_return_button)
		self.window.add_button(btn_return_text, (self.window.width - (self.window.width - self.size)/4 - btn_return_text.rect.width/2, self.window.height/5*4 - btn_return_text.rect.height/2))	

		btn_exit_text = gbgui.buttons.text_button(name = "exit_text", text = u"退出游戏", click = system.events.press_exit_button)
		self.window.add_button(btn_exit_text, (self.window.width - (self.window.width - self.size)/4 - btn_exit_text.rect.width/2, self.window.height/10*9 - btn_exit_text.rect.height/2))	
		# """for test"""
		# p = system.file_path.get_res_path('white_point.png')
		# background = pygame.image.load(p).convert_alpha()
		# self.window.screen.blit(background, [points[0][0]-18,points[0][1]-18])


	# def draw_buttons(self):
	# 	give_up_button = gbgui.buttons.text_button(name = "give_up", text = u"认输", click = system.events.press_give_up_button)
	# 	self.window.add_button(give_up_button, (self.window.width - (self.window.width - self.size)/4 - give_up_button.rect.width/2, self.window.height*4/5 - give_up_button.rect.height/2))

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