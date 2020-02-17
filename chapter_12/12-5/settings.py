# coding: GBK 
import pygame

class Settings():
    """存储所有有关12-5练习的设置"""
    def __init__(self):
        """初始化所有设置"""
        self.screen_width = 1000            # 屏幕宽度
        self.screen_height = 600            # 屏幕高度
        self.bj_color = (230, 230, 230)     # 屏幕背景颜色
        self.ship_speed_factor = 1.5        # 飞船速度调整
        self.bullet_speed_factor = 1        # 子弹速度
        self.bullet_width = 15              # 子弹宽度
        self.bullet_height = 3              # 子弹高度
        self.bullet_color = 60, 60, 60      # 子弹颜色
        self.bullets_allowed = 3            # 每次发射子弹数量上限
