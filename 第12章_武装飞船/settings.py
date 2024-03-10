class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width=900
        self.screen_heghit=600
        self.bg_color=(230,230,200)
        #飞船的设置
        self.ship_speed=30

        #子弹设置
        self.bullet_speed=2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed=3

