# -*- coding: utf-8 -*-
from enum import Enum


class GameStatues(Enum):
    # 游戏状态
    READY = 0  # 准备状态
    PLAYING = 1  # 游戏中
    OVER = 2  # 结束游戏
