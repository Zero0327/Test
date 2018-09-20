# /Users/galen/miniconda3/envs Python
# -*- coding:utf-8 -*-
# Transfer_O.py
# 万能转换器，重构
# author: Galen


class Transfer():
    '''输入输出'''
    def __init__(self, name):
        self.name = name

    def menu(self):
        '''输出选择菜单'''
        print(f'欢迎使用{self.name}'.center(30, '_'))
        menu = {
            'T': '温度转换',
            'L': '长度转换',
            'C': '货币转换'
        }
        for k, v in menu.items():
            print(f'{v}请输入{k}')

    def choose(self):
        '''输入选择转换方式'''
        choose = input('请选择转换方式：')
        if choose == 'T':
            temp_input = input('请输入温度（示例：1C或1F）')
            if temp_input.endswith('C'):
                temp = float(temp_input.strip('C'))
                Temp_T().c2f(temp)
            elif temp_input.endswith('F'):
                temp = float(temp_input.strip('F'))
                Temp_T().f2c(temp)
        elif choose == 'L':
            lenth_input = input('请输入长度（“米或英尺”示例：1米或1英尺）')
            if lenth_input.endswith('米'):
                lenth = float(lenth_input.strip('米'))
                Lenth_T().m2ft(lenth)
            elif lenth_input.endswith('英尺'):
                lenth = float(lenth_input.strip('英尺'))
                Lenth_T().ft2m(lenth)
        elif choose == 'C':
            money_input = input('请输入货币（“人民币或者美元”示例：1元或1刀）')
            if money_input.endswith('元'):
                money = float(money_input.strip('元'))
                Money_T().r2d(money)
            elif money_input.endswith('刀'):
                money = float(money_input.strip('刀'))
                Money_T().d2r(money)


class Lenth_T():
    '''长度转换'''
    def m2ft(self, lenth):
        '''米转英尺'''
        lenth_result = 3.281*lenth
        print(f'{lenth}米 = {lenth_result}英尺')

    def ft2m(self, lenth):
        '''英尺转米'''
        lenth_result = 0.3084*lenth
        print(f'{lenth}英尺 = {lenth_result}米')


class Temp_T():
    '''温度转换'''
    def f2c(self, temp):
        '''华氏转摄氏'''
        temp_result = (5/9)*(temp - 32)
        print(f'{temp}华氏度 = {temp_result}摄氏度')

    def c2f(self, temp):
        '''摄氏转华氏'''
        temp_result = (9/5)*temp + 32
        print(f'{temp}摄氏度 = {temp_result}华氏度')


class Money_T():
    '''货币转换'''
    def d2r(self, money):
        '''美元转人民币'''
        money_result = 6.3903*money
        print(f'{money}美元 = {money_result}人民币')

    def r2d(self, money):
        '''人民币转美元'''
        money_result = 1/6.3903*money
        print(f'{money}人民币 = {money_result}美元')


def main():
    origin = Transfer('万能转换器')
    origin.menu()
    origin.choose()

if __name__ == '__main__':
    main()
