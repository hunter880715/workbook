# coding: GBK 
# 创建的设置类
class Settings():
    """存储所有设置"""
    
    def __init__(self):
        """初始化设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bj_color = (0, 0, 255)
        # 速度
        self.zi_speed_factor = 1.5
