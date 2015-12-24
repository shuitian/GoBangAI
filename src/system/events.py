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
		if x.is_over(pygame.mouse.get_pos()):
			print x,"is pressed!"
			if x.name == "start":
				print "start game"
