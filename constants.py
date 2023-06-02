import os   # 导入os模块, 用于获取文件的绝对路径
import pygame

# 项目的根目录
# __file__ 当前文件的绝对路径
# os.path.dirname 获取文件的父目录, 就是项目的根目录PlaneWars
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 静态文件的目录, 存放图片, 音乐
# os.path.join 将多个路径拼接在一起
RESOURCE_DIR = os.path.join(BASE_DIR, 'resources')

# 正常游戏背景图片
BG_IMG = os.path.join(RESOURCE_DIR, 'images/background.png')

# 游戏结束背景图片
BG_IMG_OVER = os.path.join(RESOURCE_DIR, 'images/game_over.png')

# 标题图片
IMG_GAME_TITLE = os.path.join(RESOURCE_DIR, 'images/game_title.png')

# 开始图标
IMG_GAME_START = os.path.join(RESOURCE_DIR, 'images/game_start.png')
# 背景音乐
BG_MUSIC = os.path.join(RESOURCE_DIR, 'sounds/game_bg_music.mp3')

# 游戏分数的颜色
TEXT_SCORE_COLOR = pygame.Color(255, 255, 0)

# 击中小型飞机加分值
SCORE_SHOOT_SMALL = 10

# 游戏结果保存的文件地址
PLAY_RESULT_STORE_FILE = os.path.join(BASE_DIR, 'store/rect.txt')

# 我方的飞机静态资源
UOR_PLANE_IMG_LIST = [
    os.path.join(RESOURCE_DIR, 'images/hero1.png'),
    os.path.join(RESOURCE_DIR, 'images/hero2.png')
]
OUR_DESTROY_IMG_LIST = [
    os.path.join(RESOURCE_DIR, 'images/hero_broken_n1.png'),
    os.path.join(RESOURCE_DIR, 'images/hero_broken_n2.png'),
    os.path.join(RESOURCE_DIR, 'images/hero_broken_n3.png'),
    os.path.join(RESOURCE_DIR, 'images/hero_broken_n4.png'),
]

# 子弹图片
BULLET_TMG = os.path.join(RESOURCE_DIR, 'images/bullet1.png')
# 子弹发射音效
BULLET_SHOOT_TMG = os.path.join(RESOURCE_DIR, 'sounds/bullet.wav')

# 敌方小型飞机的图片和音效
SMALL_ENEMY_PLANE_IMG_LIST = [
    os.path.join(RESOURCE_DIR, 'images/enemy1.png')
]
SMALL_ENEMY_PLANE_DEST0OY_IMG_LIST = [
    os.path.join(RESOURCE_DIR, 'images/enemy1_down1.png'),
    os.path.join(RESOURCE_DIR, 'images/enemy1_down2.png'),
    os.path.join(RESOURCE_DIR, 'images/enemy1_down3.png'),
    os.path.join(RESOURCE_DIR, 'images/enemy1_down4.png'),
]
# 小型飞机坠毁的音效
SMALL_ENEMY_PLANE_DOWN_SOUND = os.path.join(RESOURCE_DIR, 'sounds/enemy1_down.wav')
