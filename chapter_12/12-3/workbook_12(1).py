# coding: GBK 
# 12-3 火箭：编写一个游戏，开始时屏幕中间有一个火箭，玩家可以使用四个方向键上下左右活动；
# 务必确保火箭不会移动到屏幕外面
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
    pygame.display.set_caption('幼紫')
    
    zi = LittleZi(ai_settings, screen)
    
    while True:
        imf.check_events(zi)
        zi.update()
        imf.update_screen(ai_settings, screen, zi)
        
run_game()

    
