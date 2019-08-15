import pygame
from plane_sprite import *


class PlaneGame(object):
    """飞机精灵"""

    # hero = Hero()

    # 初始化方法
    def __init__(self, height=700, width=480):
        print("游戏初始化...")
        # 初始化屏幕位置
        self.screen = pygame.display.set_mode((width, height))
        # 刷新率
        self.clock = pygame.time.Clock()
        # 创建精灵
        self.__create_sprites()
        # 定时器事件, 创建敌机, 发射子弹
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 200)

    # 创建精灵族
    def __create_sprites(self):
        # em1 = GameSprite("./images/enemy1.png")
        # em2 = GameSprite("./images/enemy1.png", 2)
        self.em_ground = pygame.sprite.Group()

        bg1 = Background()
        bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)

        # 创建Hero精灵
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    # 开始游戏
    def start_game(self):
        print("游戏开始...")

        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新/绘制精灵组
            self.__update_sprites()
            # 5. 更新画面
            pygame.display.update()

    # 检测碰撞
    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet_group, self.em_ground, True, True)
        sprite_list = pygame.sprite.spritecollide(self.hero, self.em_ground, False)
        if len(sprite_list) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    # 更新精灵
    def __update_sprites(self):

        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.em_ground.update()
        self.em_ground.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    # 事件处理
    def __event_handler(self):
        event_list = pygame.event.get()
        for event in event_list:
            # 1. 退出游戏事件
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                en = Enemy()
                # 将敌机精灵添加到精灵族
                self.em_ground.add(en)
            # elif event.type == pygame.KEYDOWN:
            #     # 监听keyDown事件
            #     self.__key_down(event.key)
            #     pass
            elif event.type == HERO_FIRE_EVENT:
                # 发射子弹事件
                self.hero.fire()

        # 按键连续事件
        self.__key_down2()

    # 使用get_press 获取键盘连续事件
    def __key_down2(self):
        keys_press = pygame.key.get_pressed()
        if keys_press[pygame.K_RIGHT]:
            self.hero.k_left_right = 3
            # self.hero.speed = 2
            # print("get right...")
        elif keys_press[pygame.K_LEFT]:
            self.hero.k_left_right = -3
            # self.hero.speed = -2
            # print("get left...")
        elif keys_press[pygame.K_UP]:
            self.hero.k_up_down = -3
        elif keys_press[pygame.K_DOWN]:
            self.hero.k_up_down = 3
        else:
            self.hero.speed = 0
            self.hero.k_left_right = 0
            self.hero.k_up_down = 0


    # 按键事件判断 按下事件: 仅一次
    def __key_down1(self, event_key):
        if event_key == pygame.K_RIGHT:
            print("按键向右...")
            self.hero.speed = 2
            pass
        elif event_key == pygame.K_LEFT:
            self.hero.speed = -2
            print("按键向左...")
            pass
        else:
            self.hero.speed = 0

    # 退出游戏
    @staticmethod
    def __game_over():
        print("游戏结束...")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
    
