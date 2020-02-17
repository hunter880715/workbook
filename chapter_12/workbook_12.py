# coding: GBK 
# 12-1 蓝色天空：创建一个背景为蓝色的 Pygame 窗口。
import sys
import pygame

def blue_windows():
    """初始化并建立一个窗口"""
    pygame.init()
    windows = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("蓝色天空")
    windows_color = (0, 0, 255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        windows.fill(windows_color)
        pygame.display.flip()

blue_windows()
