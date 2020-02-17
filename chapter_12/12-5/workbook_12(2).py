# coding: GBK 
# 12-5 �����������дһ����Ϸ����һ�ҷɴ�������Ļ��ߣ���������������ƶ��ɴ���
# ����Ұ��ո��ʱ���÷ɴ�����һ������Ļ�����Ҵ��е��ӵ��������ӵ��뿪��Ļ����ʧ����ɾ����
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()                                  # ��ʼ��pygame
    ai_settings = Settings()                       # ����
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # ����һ����Ļ����
    pygame.display.set_caption('���������ϰ')       # ��Ļ����
    ship = Ship(ai_settings, screen)               # ����һ�ҷɴ�ʵ��
    bullets = Group()                              # ���ڴ洢�ӵ��ı���
    
    while True:                                    # ��ʼ��Ϸ��ѭ��
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
