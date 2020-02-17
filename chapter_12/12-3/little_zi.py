# coding: GBK 
import pygame

class LittleZi():
    
    def __init__(self, ai_settings, screen):
        """��ʼ��������ͼƬλ��"""
        self.screen = screen
        self.ai_settings = ai_settings
        # ����ͼƬ����ȡ ��Ӿ���
        self.image = pygame.image.load('image/little_zi.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # ��ͼƬ������Ļ���ĵ�
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom
        # �ƶ���־
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
                
    def update(self):
        """�����ƶ���־����λ��"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1
        
        
    def blitme(self):
        """��ָ��λ�û���ͼƬ"""
        self.screen.blit(self.image, self.rect)
