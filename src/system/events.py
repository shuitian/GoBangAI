#-*- coding:utf-8 –*-
import sys,pygame,random
sys.path.append("..")
import gb.main_window
import gb.game
import gbgui.game_box
import system.player
def press_mouse_button_down(window, event):
	"""响应鼠标点击事件"""
	if event.button == 1:
		press_left_mouse_button_down(window, event)

def press_left_mouse_button_down(window, event):
	"""响应鼠标左键点击事件"""
	for [x, pos] in window.buttons:
		if x != None and x.is_over(pygame.mouse.get_pos()):
			if(x.on_click != None):
				x.on_click(window)

def press_start_button(window):
	"""开始按钮被按下"""
	window.set_background()
	game1 = gb.game.game(window)
	game1.black = window.player
	game1.white = system.player.player("bob",False).name
	window.set_game(game1)
	game1.game_box = gbgui.game_box.game_box(window)
	game1.game_box.draw_box()

def press_black_button(window):
	"""先手按钮被按下"""
	window.current_game.start_game()
	window.current_game.game_box.draw_box()	

def press_white_button(window):
	"""后手按钮被按下"""
	if not window.current_game.in_progress:
		t = window.current_game.black
		window.current_game.black = window.current_game.white
		window.current_game.white = t
		window.current_game.start_game()
		window.current_game.game_box.draw_box()
	

def press_random_button(window):
	"""先手后手随机按钮被按下"""
	r = random.randint(1, 10)
	if r >= 6:
		press_black_button(window)
	else:
		press_white_button(window)

def press_exit_button(window):
	"""退出按钮被按下"""
	sys.exit()

def press_return_button(window):
	"""返回按钮被按下"""
	press_give_up_button(window)
	window.current_game = None
	window.init()

def press_give_up_button(window):
	"""按下认输按钮"""
	if not window.current_game:
		return 
	if not window.current_game.in_progress:
		return 
	else:
		if window.current_game.black == window.player:
			window.current_game.end_game(winner = window.current_game.white)
		elif window.current_game.white == window.player:
			window.current_game.end_game(winner = window.current_game.black)
		else:
			window.current_game.end_game(winner = "None")

def press_modify_player_name(window):
	window.change_player_name()

def press_cancel_change_player_name(window):
	window.init()

def press_confirm_change_player_name(window):
	window.sql.set_last_player_name(''.join(window.new_name))
	window.init()

if __name__ == '__main__':
	r = random.randint(0, 1)
	print r