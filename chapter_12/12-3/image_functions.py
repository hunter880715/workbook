# coding: GBK 
import sys
import pygame

def check_events(zi):
    """��Ӧ���ͼ����¼�"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                zi.moving_right = True
            elif event.key == pygame.K_LEFT:
                zi.moving_left = True
            elif event.key == pygame.K_UP:
                zi.moving_up = True
            elif event.key == pygame.K_DOWN:
                zi.moving_down = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                zi.moving_right = False
            elif event.key == pygame.K_LEFT:
                zi.moving_left = False
            elif event.key == pygame.K_UP:
                zi.moving_up = False
            elif event.key == pygame.K_DOWN:
                zi.moving_down = False

def update_screen(ai_settings, screen, zi):
    """������Ļͼ���л�������Ļ"""
    screen.fill(ai_settings.bj_color)
    zi.blitme()
    pygame.display.flip()
