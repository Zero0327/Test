# /Users/galen/miniconda3/envs Python
# -*- coding:utf-8 -*-
# 51memo_O.py
# 51备忘录，重构
# author: Galen

import pickle
import re


class Memo():
    '''记录备忘录'''
    def __init__(self, name, thing, date):
        '''初始属性'''
        self.__id = 0
        self.name = name
        self.thing = thing
        self.date = date

    @property
    def id(self):
        '''id只读'''
        return self.__id

    def in_memo(self):
        '''保存输入的备忘信息字典'''
        one_memo = {
            'name': self.name,
            'thing': self.thing,
            'date': self.date
        }
        return one_memo


class MemoAdmin():
    '''管理备忘录'''
    def __init__(self):
        self.memo_list = self.load()

    def add(self):
        '''增加备忘录信息'''
        in_name = input('名称：')
        in_date = input('日期：')
        in_thing = input('事件：')
        one = Memo(in_name, in_thing, in_date).in_memo()
        self.memo_list.append(one)
        self.save()

    def delete(self):
        '''删除备忘录记录'''
        self.print_memo()
        num = input('请选择需要删除的记录编号：')
        if int(num) <= len(self.memo_list):
            self.memo_list.pop(int(num)-1)
        else:
            print('备忘录为空，请重新选择')
        self.save()

    def modify(self):
        '''修改备忘录中的日期'''
        re_date = re.compile(r'(?P<month>\d+)\.(?P<day>\d+)')
        for m in self.memo_list:
            re_date.findall(m['date'])
            m['date'] = re_date.sub(r'\g<month>月\g<day>日', m['date'])
        self.save()

    def query(self):
        '''查找备忘录中的电话号码'''
        print('找到手机号码：')
        re_phone = re.compile(r'1\d{10}$')
        for m in self.memo_list:
            print(re_phone.findall(m['thing']))

    def save(self):
        '''保存备忘录文件'''
        with open('db.pkl', 'wb') as f:
            f.write(pickle.dumps(self.memo_list))

    def load(self):
        '''从文件读取备忘录'''
        with open('db.pkl', 'rb') as f:
            self.memo_list = pickle.loads(f.read())
            return self.memo_list

    def print_memo(self):
        n = 0
        print('当前备忘信息'.center(30, '_'))
        for m in self.memo_list:
            if n != len(self.memo_list):
                n += 1
                print(f'{n}:{m}')
        print(f'共{n}条备忘记录'.center(30, '-'))


def main():
    with open('db.pkl', 'wb') as f:
        f.write(pickle.dumps([{
            'name': '手机号',
            'thing': '记录手机号13333333333',
            'date': 1.1}]))
    __author__ = 'Galen'
    desc = '51备忘录'.center(30, '-')
    print(desc)
    welcome = 'Welcome'
    print(f'{welcome}', __author__)
    menu = {
        'A': '增加备忘录',
        'D': '删除备忘录',
        'M': '修改备忘录',
        'Q': '查找备忘录',
        'E': '退出备忘录'
    }
    while(True):
        MemoAdmin().print_memo()
        for k, v in menu.items():
            print(f'【输入{k}：{v}】', end='')
        choose = input('\n请选择需要的操作：')
        if choose == 'A':
            MemoAdmin().add()
        elif choose == 'D':
            MemoAdmin().delete()
        elif choose == 'M':
            MemoAdmin().modify()
        elif choose == 'Q':
            MemoAdmin().query()
        elif choose == 'E':
            break
        else:
            print('输入错误，请重新输入\n')

if __name__ == '__main__':
    main()
