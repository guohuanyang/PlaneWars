# -*- coning: utf-8 -*-

from game.war import PlaneWar


def main():
    """游戏入口，main方法 """
    game_name = "飞机大战"  # 游戏名称
    height = 852   # 游戏窗口高度
    width = 480    # 游戏窗口宽度

    # 初始话游戏
    war = PlaneWar(game_name, height, width)
    # 添加4只小型飞机
    war.add_small_enemies(4)
    # 开启游戏
    war.run_game()


if __name__ == '__main__':
    main()
