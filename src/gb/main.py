#-*- coding:utf-8 –*-
import pygame
import main_window
from pygame.locals import *

if __name__ == '__main__':
    """实例化主窗口，并开始主循环"""
    main_window.MainWindow.window = main_window.MainWindow()
    main_window.MainWindow.window.main_loop()
