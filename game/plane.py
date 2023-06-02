# -*- coning: utf-8 -*-
import pygame

import constants
from game.bullet import Bullet


class Plane(pygame.sprite.Sprite):
    """飞机的基础类"""

    # 飞机的图片
    plane_image_src = constants.MY_PLANE_IMG
    # 飞机的爆炸的图片
    destroy_images_src = constants.MY_DESTROY_IMG_LIST
    # 坠毁的音乐地址
    down_sound_src = constants.MY_PLANE_DOWN_SOUND

    def __init__(self, left, top, speed=constants.PLANE_SPEED):
        # 调用父类的初始化方法
        super().__init__()

        # 飞机的状态，True表示飞机存活，False表示飞机坠毁
        self.active = True
        # 该飞机发射的子弹精灵组
        self.bullets = pygame.sprite.Group()

        # 加载静态资源
        self.image = None
        self.destroy_img_list = []
        self.down_sound = None
        self.load_src()

        # 飞行速度,默认5
        self.speed = speed
        # 获取飞机的位置
        self.rect = self.image.get_rect()

        # 飞机的宽度和高度
        self.plane_w, self.plane_h = self.image.get_size()

        # 改变飞机的初始化位置
        self.rect.left = left-self.plane_w/2
        self.rect.top = top

    def load_src(self):
        """加载静态资源"""
        # 飞机图像
        print(self.plane_image_src)
        self.image = pygame.image.load(self.plane_image_src)
        # 坠毁图像
        for img in self.destroy_images_src:
            self.destroy_img_list.append(pygame.image.load(img))
        # 坠毁的音乐
        self.down_sound = pygame.mixer.Sound(self.down_sound_src)

    def blit_me(self, screen):
        screen.blit(self.image, self.rect)

    def move_up(self):
        """向上移动"""
        self.rect.top -= self.speed

    def move_down(self):
        """向下移动"""
        self.rect.top += self.speed

    def move_left(self):
        """现左移动"""
        self.rect.left -= self.speed

    def move_right(self):
        """现右移动"""
        self.rect.left += self.speed

    def broken_down(self):
        """飞机坠毁效果"""
        # 1.播放坠毁音效
        if self.down_sound:
            self.down_sound.play()
        # 设置飞机状态为坠毁
        self.active = False

    def shoot(self):
        """飞机发射子弹"""
        bullet = Bullet(self.rect.centerx, self.rect.top, 18)
        self.bullets.add(bullet)


class MyPlane(Plane):
    """我方的飞机"""
    # 飞机的图片
    plane_image_src = constants.MY_PLANE_IMG
    # 飞机的爆炸的图片
    destroy_images_src = constants.MY_DESTROY_IMG_LIST
    # 坠毁的音乐地址
    down_sound_src = constants.MY_PLANE_DOWN_SOUND

    def move_up(self, miny=0):
        """限定范围"""
        super().move_up()
        if self.rect.top <= miny:
            self.rect.top = 0

    def move_down(self, maxy=500):
        """限定范围"""
        super().move_down()
        if self.rect.top >= maxy - self.plane_h:
            self.rect.top = maxy - self.plane_h

    def move_left(self, minx=0):
        """限定范围"""
        super().move_left()
        if self.rect.left <= minx:
            self.rect.left = 0

    def move_right(self, maxx=400):
        """限定范围"""
        super().move_right()
        if self.rect.left >= maxx - self.plane_w:
            self.rect.left = maxx - self.plane_w


class EnemyPlane(Plane):
    """敌方飞机"""
    # 飞机的图片
    plane_image_src = constants.ENEMY_PLANE_IMG
    # 飞机的爆炸的图片
    destroy_images_src = constants.ENEMY_PLANE_DEST0OY_IMG_LIST
    # 坠毁的音乐地址
    down_sound_src = constants.ENEMY_PLANE_DOWN_SOUND

    def move_down(self):
        super().move_down()