# coding: GBK 
import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(r'image/ship.bmp')  # 读取文件图像初始化
        self.rect = self.image.get_rect()                  # 初始化文件图像矩形
        self.screen_rect = screen.get_rect()               # 初始化文件外接屏幕矩形
        self.rect.centery = self.screen_rect.centery       # 确定屏幕中心点处于y轴
        self.rect.left = self.screen_rect.left        # 确定图像文件位于屏幕左侧中间
        self.centery = float(self.rect.centery)        # 在飞船属性screen中存储小数
        self.centerx = float(self.rect.centerx)       # 在飞船属性screen1中存储小数
        self.moving_up = False                             # 向上移动标志
        self.moving_down = False                           # 向下移动标志
        self.moving_right = False                          # 向右移动标志
        self.moving_left = False                           # 向左移动标志
    
    def update(self):
        """根据移动调整飞船位置"""
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        
        self.rect.centery = self.centery
        self.rect.centerx = self.centerx
        
    def blitme(self):
        """将文件图像绘制到指定位置"""
        self.screen.blit(self.image, self.rect)
