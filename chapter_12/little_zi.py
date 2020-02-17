# coding: GBK 
import pygame

class LittleZi():
    
    def __init__(self, windows):
        """��ʼ��������ͼƬλ��"""
        self.windows = windows
        # ����ͼƬ����ȡ ��Ӿ���
        self.image = pygame.image.load('image/little_zi.bmp')
        self.rect = self.image.get_rect()
        self.windows_rect = windows.get_rect()
        # ��ͼƬ������Ļ���ĵ�
        self.rect.center = self.windows_rect.center
        self.rect.bottom = self.windows_rect.bottom
        
    def blitme(self):
        """��ָ��λ�û���ͼƬ"""
        self.windows.blit(self.image, self.rect)
