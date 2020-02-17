# coding: GBK 
import pygame

class LittleZi():
    
    def __init__(self, windows):
        """初始化并设置图片位置"""
        self.windows = windows
        # 加载图片并获取 外接矩形
        self.image = pygame.image.load('image/little_zi.bmp')
        self.rect = self.image.get_rect()
        self.windows_rect = windows.get_rect()
        # 将图片放在屏幕中心点
        self.rect.center = self.windows_rect.center
        self.rect.bottom = self.windows_rect.bottom
        
    def blitme(self):
        """在指定位置绘制图片"""
        self.windows.blit(self.image, self.rect)
