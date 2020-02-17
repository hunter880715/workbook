# coding: GBK 
# 12-3 �������дһ����Ϸ����ʼʱ��Ļ�м���һ���������ҿ���ʹ���ĸ�������������һ��
# ���ȷ����������ƶ�����Ļ����
import sys
import pygame
from settings import Settings
from little_zi import LittleZi
import image_functions as imf

def run_game():
    
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('����')
    
    zi = LittleZi(ai_settings, screen)
    
    while True:
        imf.check_events(zi)
        zi.update()
        imf.update_screen(ai_settings, screen, zi)
        
run_game()

    
