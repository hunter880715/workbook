# coding: GBK 
import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        """��ʼ���ɴ������ó�ʼλ��"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load(r'image/ship.bmp')  # ��ȡ�ļ�ͼ���ʼ��
        self.rect = self.image.get_rect()                  # ��ʼ���ļ�ͼ�����
        self.screen_rect = screen.get_rect()               # ��ʼ���ļ������Ļ����
        self.rect.centery = self.screen_rect.centery       # ȷ����Ļ���ĵ㴦��y��
        self.rect.left = self.screen_rect.left        # ȷ��ͼ���ļ�λ����Ļ����м�
        self.centery = float(self.rect.centery)        # �ڷɴ�����screen�д洢С��
        self.centerx = float(self.rect.centerx)       # �ڷɴ�����screen1�д洢С��
        self.moving_up = False                             # �����ƶ���־
        self.moving_down = False                           # �����ƶ���־
        self.moving_right = False                          # �����ƶ���־
        self.moving_left = False                           # �����ƶ���־
    
    def update(self):
        """�����ƶ������ɴ�λ��"""
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
        """���ļ�ͼ����Ƶ�ָ��λ��"""
        self.screen.blit(self.image, self.rect)
