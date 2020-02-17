# coding: GBK 
import sys
import pygame

def check_events():
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
def update_windows(ai_set, windows, little_zi):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重绘屏幕
    windows.fill(ai_set.bj_color)
    little_zi.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()
