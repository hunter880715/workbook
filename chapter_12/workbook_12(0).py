# coding: GBK 
# 12-2 ��Ϸ��ɫ�����·���ϲ������Ϸ��ɫλͼͼ���һ��ͼ��ת��Ϊλͼ��
# ����һ���࣬���ý�ɫ���Ƶ���Ļ���룬������ͼ��ı���ɫ����Ϊ��Ļ����ɫ��������ɫ��֮��
import sys
import pygame
from settings import *
from little_zi import *
import image_functions as es

def blue_windows():
    """��ʼ��������һ������"""
    pygame.init()
    ai_set = Settings()
    windows = pygame.display.set_mode(
        (ai_set.windows_width, ai_set.windows_height))
    pygame.display.set_caption("��ɫ���")
    # ����ͼƬ
    little_zi = LittleZi(windows)
    # ��ѭ��
    while True:
        es.check_events()
        es.update_windows(ai_set, windows, little_zi)

blue_windows()
