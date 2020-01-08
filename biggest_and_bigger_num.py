# ！/usr/bin/env python
# -*- coding:utf-8 -*-
# author: peterZhi time:2020/1/6
#使用文本数据输入，显示出最大值与次大值
num=eval(input("Input numbers:"))
print(num)
next_max=max=eval(input())
for i in range(num-1):
    data=eval(input())
    if  max < data:
        next_max=max;max = data
    elif max > data:
        if next_max < data:
            next_max=data
        else:
            pass
    else:
        pass
print("Max number:",max)
print("Second max number:",next_max)
