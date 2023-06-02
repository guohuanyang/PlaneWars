# -*- coning: utf-8 -*-
import sys
from enum import Enum

import pygame

import constants
from game.plane import OurPlane, SmallEnemyPlane


class GameStatues(Enum):
    # 游戏状态
    READY = 0  # 准备状态
    PLAYING = 1  # 游戏中
    OVER = 2  # 结束游戏


class PlaneWar:
    """飞机大战"""

    def __init__(self, game_name, height=852, width=480):
        pygame.init()
        # 游戏状态
        self.status = GameStatues.READY

        self.frame = 0  # 播发帧数
        self.clock = pygame.time.Clock()

        # 一架飞机可以属于多个精灵组
        self.small_enemies = pygame.sprite.Group()
        # 游戏结果
        self.score = 0

        self.width, self.height = width, height
        # 屏幕对象,设计窗口大小
        self.screen = pygame.display.set_mode((self.width, self.height))
        # 设计窗口标题
        pygame.display.set_caption(game_name)
        # 加载背景图片
        self.bg = pygame.image.load(constants.BG_IMG)
        self.bg_over = pygame.image.load(constants.BG_IMG_OVER)
        # 游戏标题
        self.img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
        self.img_game_title_rect = self.img_game_title.get_rect()
        # 获取游戏标题的宽和高
        self.t_width, self.t_height = self.img_game_title.get_size()
        # 居中
        self.img_game_title_rect.topleft = (
            int((self.width - self.t_width) / 2), int((self.height - self.t_height) / 2 - 40))

        # 开始按钮
        self.btn_start = pygame.image.load(constants.IMG_GAME_START)
        self.btn_start_rect = self.btn_start.get_rect()
        self.btn_width, self.btn_height = self.btn_start.get_size()
        # 居中
        self.btn_start_rect.topleft = (int((self.width - self.btn_width) / 2), int((self.height / 2 + self.btn_height)))

        # 设置游戏文字对象 系统字体华文隶书，字号32
        self.score_font = pygame.font.SysFont('华文隶书', 32)

        # 加载背景音乐
        pygame.mixer.music.load(constants.BG_MUSIC)

        # 加载游戏音效，就是播放音乐，-1代表循环播放
        pygame.mixer.music.play(-1)
        # 设置音乐音量0-1，0代表静音，1代表最大音量
        pygame.mixer.music.set_volume(.2)

        # 我方飞机对象
        self.my_plane = OurPlane(self.screen, speed=5)

        # self.clock = pygame.time.Clock()
        # 记录键盘上的某一个,用于控制飞机
        self.key_down = None

    def bind_event(self):
        """绑定事件"""
        # 1.监听事件
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                # pygame游戏界面退出
                pygame.quit()
                # 程序退出
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:   # 鼠标按下事件
                # 鼠标点击进入游戏
                # 游戏正在准备中，点击才能进入游戏
                if self.status == GameStatues.READY:
                    self.status = GameStatues.PLAYING
                elif self.status == GameStatues.PLAYING:
                    # 游戏状态中，点击鼠标发射子弹
                    self.my_plane.shoot()
                elif self.status == GameStatues.OVER:
                    self.status = GameStatues.READY
                    self.add_small_enemies(6)
            elif event.type == pygame.KEYDOWN:
                # 键盘事件
                self.key_down = event.key
                # 游戏中，才需要控制键盘AWSD
                if self.status == GameStatues.PLAYING:
                    # W 或者 ⬆️ 向上移动
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.my_plane.move_up()

                    # S 或者 ⬇️ 向下移动
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.my_plane.move_down()

                    # A 或者 ⬅️ 向左移动
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.my_plane.move_left()

                    # D 或者 ➡️ 向右移动
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.my_plane.move_rige()

                    # 空格键发射子弹
                    elif event.key == pygame.K_SPACE:
                        self.my_plane.shoot()

    def add_small_enemies(self, num):
        """
        随机生成N架小型敌机
        :param num: 飞机的生产数量
        :return:
        """
        # 随机生成num架小型飞机
        for i in range(num):
            plane = SmallEnemyPlane(self.screen, 5)
            plane.add(self.small_enemies)

    def run_game(self):
        """游戏主循环部分"""
        while True:
            # 1.设计帧数
            self.clock.tick(60)
            self.frame += 1
            if self.frame >= 60:
                self.frame = 0
            # 2.绑定事件
            self.bind_event()

            # 3.更新游戏状态
            if self.status == self.READY:
                self.screen.blit(self.bg, self.bg.get_rect())
                #标题
                self.screen.blit(self.img_game_title, self.img_game_title_rect)
                #开始按钮
                self.screen.blit(self.btn_start, self.btn_start_rect)
                self.key_down = None
            elif self.status == self.PLAYING:
                # 游戏进行中
                # 绘制背景
                self.screen.blit(self.bg, self.bg.get_rect())
                # 绘制飞机
                self.my_plane.update(self)
                # 绘制子弹
                self.my_plane.bullets.update(self)
                # 绘制敌方飞机
                self.small_enemies.update()
                # 游戏分数
                score_text = self.score_font.render(
                    '得分: {0}'.format(self.rest.score),
                    False,
                    constants.TEXT_SCORE_COLOR
                )
                self.screen.blit(score_text, score_text.get_rect())
            elif self.status == self.OVER:
                # 游戏结束
                # 游戏背景
                self.screen.blit(self.bg_over, self.bg_over.get_rect())
                # 分数统计
                # 1. 本次总分
                score_text = self.score_font.render(
                    '{0}'.format(self.rest.score),
                    False,
                    constants.TEXT_SCORE_COLOR
                )
                score_text_rect = score_text.get_rect()
                text_w, text_h = score_text.get_size()
                # 改变文字的位置
                score_text_rect.topleft = (
                    int((self.width - text_h) / 2),
                    int(self.height / 2)
                )
                self.screen.blit(score_text, score_text_rect)
                # 2. 历史最高分
                score_his = self.score_font.render(
                    '{0}'.format(self.rest.get_max_core()),
                    False,
                    constants.TEXT_SCORE_COLOR
                )
                self.screen.blit(score_his, (150, 40))

            pygame.display.flip()
