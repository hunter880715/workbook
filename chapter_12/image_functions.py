# coding: GBK 
import sys
import pygame

def check_events():
    """��Ӧ���ͼ����¼�"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
def update_windows(ai_set, windows, little_zi):
    """������Ļ�ϵ�ͼ�񣬲��л�������Ļ"""
    # ÿ��ѭ�����ػ���Ļ
    windows.fill(ai_set.bj_color)
    little_zi.blitme()
    # ��������Ƶ���Ļ�ɼ�
    pygame.display.flip()
