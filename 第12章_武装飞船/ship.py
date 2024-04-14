import pygame
from settings import Settings
from pygame.sprite import Sprite
class Ship(Sprite):
    """管理飞船的类"""
    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置"""
        """接受两个参数，除了self引用，还有一个指向AlienInvasiom实例的引用"""
        super().__init__()
        self.screen=ai_game.screen # 将屏幕赋给Ship的一个属性
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()# 屏幕位置外接矩形

        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()# 飞船位置外接矩形

        #每艘新飞船都放在屏幕底部的中央
        self.rect.midbottom=self.screen_rect.midbottom
        """ 屏幕位置外接矩形中央坐标=飞船位置外接矩形中央坐标"""

        #在飞船的属性x中存储一个浮点数
        self.x=float(self.rect.x)

        #移动标志（飞船一开始不动）
        self.moving_right=False
        self.moving_left=False

        #飞船的位置移动速度
        self.ship_speed=1.5

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed

        self.rect.x=self.x
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """将飞船放置在屏幕底部的中央"""
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)
