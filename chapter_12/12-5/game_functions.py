# coding: GBK 
import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键按下"""
    if event.key == pygame.K_UP:
        ship.moving_up = True          # 飞船沿着坐标y轴向上移动
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True        # 飞船沿着坐标y轴向下移动
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True       # 飞船沿着坐标x轴向右移动
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True        # 飞船沿着坐标x轴向左移动
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果子弹没有达到上限，就再发射一颗"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)    # 创建一颗子弹，将其添加到编组bullets中
        
def check_keyup_events(event, ship):
    """响应按键松开"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """响应按键与鼠标事件"""
    for event in pygame.event.get():           # 监控鼠标和键盘事件
        if event.type == pygame.QUIT:
            sys.exit()                         # 退出游戏
        elif event.type == pygame.KEYDOWN:     # 出发按键KEYDOWN事件
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.right >= 1000:
            bullets.remove(bullet)

def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕图像，并切换到新屏幕"""
    screen.fill(ai_settings.bj_color)          # 屏幕填充背景颜色
    for bullet in bullets.sprites():           # 在飞船和外星人后面重绘所有子弹
        bullet.draw_bullet()
    ship.blitme()                              # 绘制飞船
    pygame.display.flip()                      # 让每次循环新绘制的屏幕可见
