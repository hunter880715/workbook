# coding: GBK 
import pygame

class Settings():
    """�洢�����й�12-5��ϰ������"""
    def __init__(self):
        """��ʼ����������"""
        self.screen_width = 1000            # ��Ļ���
        self.screen_height = 600            # ��Ļ�߶�
        self.bj_color = (230, 230, 230)     # ��Ļ������ɫ
        self.ship_speed_factor = 1.5        # �ɴ��ٶȵ���
        self.bullet_speed_factor = 1        # �ӵ��ٶ�
        self.bullet_width = 15              # �ӵ����
        self.bullet_height = 3              # �ӵ��߶�
        self.bullet_color = 60, 60, 60      # �ӵ���ɫ
        self.bullets_allowed = 3            # ÿ�η����ӵ���������
