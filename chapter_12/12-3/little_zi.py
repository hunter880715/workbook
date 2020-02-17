# coding: GBK 
import pygame

class LittleZi():
    
    def __init__(self, ai_settings, screen):
        """初始化并设置图片位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载图片并获取 外接矩形
        self.image = pygame.image.load('image/little_zi.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将图片放在屏幕中心点
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
                
    def update(self):
        """根据移动标志调整位置"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1
        
        
    def blitme(self):
        """在指定位置绘制图片"""
        self.screen.blit(self.image, self.rect)
