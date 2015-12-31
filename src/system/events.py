#-*- coding:utf-8 –*-
import sys,pygame
sys.path.append("..")
import gb.main_window
import gbgui.game_box
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
	"""开始按钮被按下"""
	window.set_background()
	box = gbgui.game_box.game_box(window)
	box.draw_box()

def press_exit_button(window):
	"""退出按钮被按下"""
	sys.exit()