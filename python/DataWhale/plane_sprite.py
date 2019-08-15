import random
import pygame


# 刷新帧率
FRAME_PER_SEC = 60
# 屏幕属性
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 创建敌军事件
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建英雄发射子弹事件
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name_load, speed=1):

        # 1, 调用父类的方法 super().__init__()
        super().__init__()

        # 2. 图像位置速度
        self.image = pygame.image.load(image_name_load)
        # 获取图像的位置
        self.rect = self.image.get_rect()
        # 赋值速度
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed
        # # 判断位置, 超出部分, 重置精灵起始位置
        # if self.rect.y >= SCREEN_RECT.height:
        #     self.rect.y = SCREEN_RECT.y


class Background(GameSprite):
    """游戏背景精灵"""
    def update(self):
        # 1. 调用父类方法实现
        super().update()
        # 2. 判断是移除屏幕, 将图像摄者到图像上方

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height

    def __init__(self, is_alt=False):
        """"""
        # 1. 调用父类方法创建精灵, 创建背景图片
        super().__init__("./images/background.png")
        # 2. 判断is_alt 修改图像位置
        if is_alt:
            self.rect.y = -SCREEN_RECT.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 初始化父类方法
        super().__init__("./images/enemy1.png")

        # 指定敌机的初始随机速度
        random_speed = random.randint(1, 3)
        self.speed = random_speed

        # 敌机初始随机位置, 最大值获取
        max_x = SCREEN_RECT.width-self.rect.width
        # 设置 x 的位置
        self.rect.x = random.randint(0, max_x)

        # 设置 Y 方向初始位置
        self.rect.bottom = 0

    def update(self):
        # 调用父类方法保持垂直方向飞行
        super().update()
        # 判断是否飞出屏幕, 如果飞出, 需要从精灵族删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # print("飞出屏幕, 需要删除...")
            # 删除精灵
            # self.__del__()
            # sprite 提供的kill()方法, 会将精灵在精灵族和内存中删除, 同时也调用__del__方法
            self.kill()

    # def __del__(self):
    #     # print("销毁敌机: %s" % self.rect)
    #     pass


class Hero(GameSprite):
    """英雄"""

    def __init__(self, key_up_down=0, key_left_right=0):
        # 调用父类方法
        super().__init__("./images/me1.png", 0)
        # 设置英雄位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.k_up_down = key_up_down
        self.k_left_right = key_left_right
        self.bullet_group = pygame.sprite.Group()
        pass

    def update(self):
        # 英雄在水平方向上运动
        self.rect.y += self.k_up_down
        self.rect.x += self.k_left_right
        # 设置水平方向的运行轨迹界限
        if self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.x <= 0:
            self.rect.x = 0
        # 试着垂直方向上的运行轨迹界限
        if self.rect.bottom >= SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom
        elif self.rect.y <= 0:
            self.rect.y = 0

    def fire(self):
        # print("发射子弹... ")
        # 创建子弹
        bu = Bullet()
        # 子弹位置
        bu.rect.bottom = self.rect.y
        bu.rect.centerx = self.rect.centerx
        # 添加到精灵族
        self.bullet_group.add(bu)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        # 创建子弹
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        # 调用父类方法, 子弹严垂直方向飞行
        super().update()
        # 越界, 删除精灵
        if self.rect.bottom <= 0:
            self.kill()

    def __del__(self):
        print("bullet kill...")
        
        
      
