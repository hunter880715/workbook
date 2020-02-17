# coding: GBK 
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """�ɴ��ӵ��������"""
    def __init__(self, ai_settings, screen, ship):
        """�ڷɴ�������λ�ô���һ���ӵ�����"""
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
            ai_settings.bullet_height)
        self.rect.centery = ship.rect.centery  # ���ӵ������ƶ����ɴ��������
        self.rect.right = ship.rect.right
        self.x = float(self.rect.x)            # �洢��С����ʾ���ӵ�λ��
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """�����ƶ��ӵ�"""
        self.x += self.speed_factor
        self.rect.x = self.x
        
    def draw_bullet(self):
        """����Ļ�ϻ����ӵ�"""
        pygame.draw.rect(self.screen, self.color, self.rect)
