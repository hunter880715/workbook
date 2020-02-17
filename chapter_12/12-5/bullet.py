# coding: GBK 
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """飞船子弹管理的类"""
    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
            ai_settings.bullet_height)
        self.rect.centery = ship.rect.centery  # 将子弹矩形移动到飞船的坐标点
        self.rect.right = ship.rect.right
        self.x = float(self.rect.x)            # 存储用小数表示的子弹位置
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """向右移动子弹"""
        self.x += self.speed_factor
        self.rect.x = self.x
        
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
