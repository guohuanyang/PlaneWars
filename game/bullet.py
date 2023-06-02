# -*- coning: utf-8 -*-
import pygame
import constants


class Bullet(pygame.sprite.Sprite):
    """
    子弹类
    cneterx: x轴坐标
    top: y轴坐标
    speed: 子弹的速度
    """
    def __init__(self, centerx, top, speed=constants.BULLET_SPEED):

        super().__init__()
        # 子弹速度, 默认10
        self.speed = speed
        # 加载子弹
        self.image = pygame.image.load(constants.BULLET_TMG)
        # 获取子弹区域
        self.rect = self.image.get_rect()

        # 设置子弹的位置,把子弹的位置设置在飞机头
        self.rect.centerx = centerx
        self.rect.top = top

        # 发射的音效
        self.shoot_sound = pygame.mixer.Sound(constants.BULLET_SHOOT_TMG)
        self.shoot_sound.set_volume(0.3)
        self.shoot_sound.play()

    def update(self):
        """"更新子弹位置"""
        self.rect.top -= self.speed
        # 超出屏幕范围
        if self.rect.top <= 0:
            self.remove()

