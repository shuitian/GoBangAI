#-*- coding:utf-8 –*-
import sys,pygame
sys.path.append("..")
import gb.main_window
def press_mouse_button_down(window, event):
	"""响应鼠标点击事件"""
	if event.button == 1:
		press_left_mouse_button_down(window, event)

def press_left_mouse_button_down(window, event):
	"""响应鼠标左键点击事件"""
	for x in window.buttons:
		if x != None and x.is_over(pygame.mouse.get_pos()):
			if(x.on_click != None):
				x.on_click(window)

def press_start_button(window):
	print "start"
	window.clear_button()
	window.set_background()
	drawlines(window)

def drawlines(window):
	edge_color = (150,118,75)
	line_color = (0,0,0)
	length = 10
	size = 720
	nr_lines = 17
	space = size/(nr_lines+1)
	for x in xrange(1,nr_lines+1):
		start_pot = ((window.width-size)/2,(window.height-size)/2 + x*space)
		end_pot = ((window.width+size)/2,(window.height-size)/2 + x*space)
		pygame.draw.line(window.screen, line_color, start_pot, end_pot, 2)

		start_pot = ((window.width-size)/2 + x*space,(window.height-size)/2)
		end_pot = ((window.width-size)/2 + x*space,(window.height+size)/2)
		pygame.draw.line(window.screen, line_color, start_pot, end_pot, 2)
	pygame.draw.rect(window.screen, edge_color, ((window.width-size)/2,(window.height-size)/2,size,size), 10)

def press_exit_button(window):
	print "exit"
	sys.exit()