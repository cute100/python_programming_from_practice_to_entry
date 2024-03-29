import sys #首先导入sys模块，sys模块包含退出功能暨当玩家退出游戏时使用sys模块中的工具来退出游戏、
import pygame #导入pygame模块，pygame模块包含开发有序所需的功能。
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion: #创建一个名为AlienInvasion的类。
    def __init__(self):
        """初始化游侠并创建游戏资源"""
        pygame.init() #调用pygame.init()初始化背景，让pygame能够正常的工作。
        self.clock=pygame.time.Clock()

        self.setting=Settings()

        # self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.setting.screen_width=self.screen.get_rect().width
        # self.setting.screen_heghit=self.screen.get_rect().height
        self.screen=pygame.display.set_mode((self.setting.screen_width,self.setting.screen_heghit))

        # self.bg_color=(230,230,230)
        # self.screen=pygame.display.set_mode((1200,800))#调用pygame.display.set_mode创建一个显示窗口并指定窗口的尺寸--宽1200像素
        # # 、高800像素，然后将这个显示的窗口赋给self.screen,让这个类的所有方法都能够使用它。赋给self.surface的对象是一个surface。在pygame中
        # #surface是屏幕的一部分，用于显示游戏元素。在这个游戏中，每个元素（如外星人或飞船）都是一个surface。display.set_mode()返回的surface
        # #表示整个游戏窗口，激活游戏的动画循环后，每经果一次循环将自动重新绘画这个surface，将用户输入触发的有所有变化都反映出来。



        pygame.display.set_caption("Alien Invasion")#设置当前窗口标题Alien Invasion。
        self.bg_color=(self.setting.bg_color)

        self.ship=Ship(self)

        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):#这个游戏由run_game()控制
        """开始游戏的主循环"""
        while True:
            self._check_enent()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _create_fleet(self):
        """创建一个外星舰队"""
        #创建一个外星人,再不断添加，直到没有空间添加外星人为止
        #外星人的间距为外星人的宽度
        alien=Alien(self)
        alien_width,alien_height=alien.rect.size
        current_x,current_y=alien_width,alien_height
        while current_y<(self.setting.screen_heghit-3*alien_height):
            while current_x < (self.setting.screen_width - 2 * alien_width):
                self._crate_alien(current_x,current_y)
                current_x+=2*alien_width

            #添加一行外星人后，重置x值并递增y值
            current_x=alien_width
            current_y+=2*alien_width


    def _crate_alien(self,x_position,y_position):
        """创建一个外星人并将其放在当前行中"""
        new_alien=Alien(self)
        new_alien.x=x_position
        new_alien.rect.x=x_position
        new_alien.rect.y=y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """更新外星舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

    def _update_bullets(self):
        """更新子弹位置并删除已消失的子弹"""
        #更新子弹的位置
        self.bullets.update()
        #删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)
        print(len(self.bullets))
    def _check_enent(self):
            #倾听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    def _check_keydown_events(self,event):
            if event.key==pygame.K_RIGHT:
                self.ship.moving_right=True
            elif event.key==pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key==pygame.K_ESCAPE:
                sys.exit()
            elif event.key==pygame.K_SPACE:
                self._fire_bullet()
    def _check_keyup_events(self, event):
            if event.key==pygame.K_RIGHT:
                self.ship.moving_right=False
            elif event.key==pygame.K_LEFT:
                self.ship.moving_left=False
    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets"""
        if len(self.bullets)<self.setting.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
    def _update_screen(self):
        # 每次循环时都重绘屏幕
        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        #让最近绘制的屏幕可见
        pygame.display.flip()
        self.clock.tick(60)

    def _check_fleet_edges(self):
        """在有万星人到达边沿时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整个舰队向下移动，并改变他们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y+=self.setting.fleet_drop_speed
        self.setting.fleet_direction*=-1


if __name__=="__main__":
    """创建游戏实例并运行游戏"""
    ai=AlienInvasion() #创建实例并调用run_game()。
    ai.run_game() #实例调用run_game()。

