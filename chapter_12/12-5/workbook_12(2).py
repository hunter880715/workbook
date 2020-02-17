# coding: GBK 
# 12-5 侧面射击：编写一个游戏，将一艘飞船放在屏幕左边，并允许玩家上下移动飞船。
# 在玩家按空格键时，让飞船发射一颗在屏幕中向右穿行的子弹，并在子弹离开屏幕而消失后将其删除。
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()                                  # 初始化pygame
    ai_settings = Settings()                       # 设置
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # 创建一个屏幕对象
    pygame.display.set_caption('侧面射击练习')       # 屏幕标题
    ship = Ship(ai_settings, screen)               # 创建一艘飞船实例
    bullets = Group()                              # 用于存储子弹的编组
    
    while True:                                    # 开始游戏主循环
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
