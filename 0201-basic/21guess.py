# /Users/galen/miniconda3/envs Python
# -*- coding:utf-8 -*-
# 21guess.py
# 21guess game
# author: Galen

import random

"""
- 两个玩家，游戏开始先输入名字
- 用字典保存每个玩家的信息：姓名，获胜次数
- 电脑随机产生2个数，每个玩家轮流猜一次，与电脑随机两个数求和，最接近21的获胜
- 每轮结束显示玩家信息
- 按q退出游戏
"""
target = 21
print('欢迎进入21点游戏'.center(30, '-'))

player1 = input('请输入第一个玩家名字：')
player2 = input('请输入第二个玩家名字：')

players = {
    player1:
    {'win': 0},
    player2:
    {'win': 0}
}

game_over = True

while(game_over):
    num1 = random.randint(1, 13)
    num2 = random.randint(1, 13)

    player1_guess = input('请玩家1猜数字：')
    player2_guess = input('请玩家2猜数字：')
    sum1 = int(num1) + int(num2) + int(player1_guess)
    sum2 = int(num1) + int(num2) + int(player2_guess)
    print(f'随机数为：{num1}和{num2}，{player1}之和为：{sum1}， {player2}之和为：{sum2}')

    if abs(sum1 - target) > abs(sum2 - target):
        players[player2]['win'] += 1
        sum_win2 = players[player2]['win']
        print(f'{player2}获胜，获胜次数为：{sum_win2}')
    elif abs(sum1 - 21) == abs(sum2 - 21):
        print('平局'.center(30, '-'))
    else:
        players[player1]['win'] += 1
        sum_win1 = players[player1]['win']
        print(f'{player1}获胜，获胜次数为：{sum_win1}')
    print('按q退出，任意键继续')
    game_over = input().strip() != 'q'
print('再见'.center(30, '-'))
