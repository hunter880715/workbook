# coding: GBK 
# 12-1 ��ɫ��գ�����һ������Ϊ��ɫ�� Pygame ���ڡ�
import sys
import pygame

def blue_windows():
    """��ʼ��������һ������"""
    pygame.init()
    windows = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("��ɫ���")
    windows_color = (0, 0, 255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        windows.fill(windows_color)
        pygame.display.flip()

blue_windows()
