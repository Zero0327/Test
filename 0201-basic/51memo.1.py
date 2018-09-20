#!/Users/galen/miniconda3/envs Python
# -*- coding:utf-8 -*-
# 51memo.1.py
# memo demo
# author: Galen

from color_me import ColorMe

__author__ = 'Galen'

desc = '51备忘录'.center(30, '-')
print(desc)
welcome = 'Welcome'
print(f'{welcome}', __author__)
print('请输入备忘信息：')

all_memo = []

is_add = True
while(is_add):
    in_memo = input('请直接输入需要添加的事件（示例：早上叫我起床）：')
    one = {}
    time_dict = {
        '中午': '12',
        '早上': '8',
        '下午': '17'
    }
    if in_memo.find('点') != -1:
        one['time'] = in_memo[in_memo.find('点')-1:in_memo.find('点')]
        one['thing'] = in_memo[in_memo.find('点')+1:]
    elif in_memo.find('中午') != -1:
        one['time'] = time_dict['中午']
        one['thing'] = in_memo[in_memo.find('中午')+2:]
    elif in_memo.find('早上') != -1:
        one['time'] = time_dict['早上']
        one['thing'] = in_memo[in_memo.find('早上')+2:]
    elif in_memo.find('下午') != -1:
        one['time'] = time_dict['下午']
        one['thing'] = in_memo[in_memo.find('下午')+2:]
    else:
        print('输入错误')
    all_memo.append(one)
    num = 0
    for x in all_memo:
        time = ColorMe(x['time'] + '点').blue()
        thing = ColorMe(x['thing']).red()
        num += 1
        print(f'第{num}条->时间：{time}，事件：{thing}')
    print(f'共添加{len(all_memo)}条任务', end='')
    print('（y：继续添加，任意键退出）')
    is_add = input().strip() == 'y'
print('再见'.center(30, '-'))
