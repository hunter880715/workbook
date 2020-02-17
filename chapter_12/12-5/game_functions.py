# coding: GBK 
import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """��Ӧ��������"""
    if event.key == pygame.K_UP:
        ship.moving_up = True          # �ɴ���������y�������ƶ�
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True        # �ɴ���������y�������ƶ�
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True       # �ɴ���������x�������ƶ�
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True        # �ɴ���������x�������ƶ�
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """����ӵ�û�дﵽ���ޣ����ٷ���һ��"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)    # ����һ���ӵ���������ӵ�����bullets��
        
def check_keyup_events(event, ship):
    """��Ӧ�����ɿ�"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """��Ӧ����������¼�"""
    for event in pygame.event.get():           # ������ͼ����¼�
        if event.type == pygame.QUIT:
            sys.exit()                         # �˳���Ϸ
        elif event.type == pygame.KEYDOWN:     # ��������KEYDOWN�¼�
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right >= 1000:
            bullets.remove(bullet)

def update_screen(ai_settings, screen, ship, bullets):
    """������Ļͼ�񣬲��л�������Ļ"""
    screen.fill(ai_settings.bj_color)          # ��Ļ��䱳����ɫ
    for bullet in bullets.sprites():           # �ڷɴ��������˺����ػ������ӵ�
        bullet.draw_bullet()
    ship.blitme()                              # ���Ʒɴ�
    pygame.display.flip()                      # ��ÿ��ѭ���»��Ƶ���Ļ�ɼ�
