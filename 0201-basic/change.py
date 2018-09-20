#!/Users/galen/miniconda3/envs Python
# -*- coding:utf-8 -*-
# 51memo.1.py
# demo
# author: Galen

print('欢迎使用万能转换器'.center(30, '#'))
menu = {
    'T': '温度转换',
    'L': '长度转换',
    'C': '货币转换'
}
for k, v in menu.items():
    print(f'{v}请输入{k}'.center(30, '~'))
choose = input('请选择转换类型：')
if choose == 'T':
    temp = input('请输入温度（示例：1C或1F）')
    if temp.endswith('C'):
        temp = float(temp.strip('C'))
        Tf = (9/5)*temp + 32
        print(f'{temp}摄氏度 = {Tf}华氏度')
    elif temp.endswith('F'):
        temp = float(temp.strip('F'))
        Tc = (5/9)*(temp - 32)
        print(f'{temp}华氏度 = {Tc}摄氏度')
    else:
        print('输入错误')
elif choose == 'L':
    lenth = input('请输入长度（“米或英尺”示例：1m或1ft）')
    if lenth.endswith('m'):
        lenth = float(lenth.strip('m'))
        ft = 3.281*lenth
        print(f'{lenth}米 = {ft}英尺')
    elif lenth.endswith('ft'):
        lenth = float(lenth.strip('ft'))
        mi = 0.3084*lenth
        print(f'{lenth}英尺 = {mi}米')
    else:
        print('输入错误')
elif choose == 'C':
    money = input('请输入货币（“人民币或者美元”示例：1元或1刀）')
    if money.endswith('元'):
        money = float(money.strip('元'))
        doller = 1/6.3903*money
        print(f'{money}元 = {doller}刀')
    elif money.endswith('刀'):
        money = float(money.strip('刀'))
        rmb = 6.3903*money
        print(f'{money}刀 = {rmb}元')
    else:
        print('输入错误')
else:
    print('输入错误')
