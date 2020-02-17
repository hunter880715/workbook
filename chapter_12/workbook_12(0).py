# coding: GBK 
# 12-2 游戏角色：找衣服你喜欢的游戏角色位图图像或将一副图像转换为位图。
# 创建一个类，将该角色绘制到屏幕中央，并将该图像的背景色设置为屏幕背景色，或是颜色反之。
import sys
import pygame
from settings import *
from little_zi import *
import image_functions as es

def blue_windows():
    """初始化并建立一个窗口"""
    pygame.init()
    ai_set = Settings()
    windows = pygame.display.set_mode(
        (ai_set.windows_width, ai_set.windows_height))
    pygame.display.set_caption("蓝色天空")
    # 创建图片
    little_zi = LittleZi(windows)
    # 主循环
    while True:
        es.check_events()
        es.update_windows(ai_set, windows, little_zi)

blue_windows()
