# ！/usr/bin/env python 
# -*- coding:utf-8 -*-
# author: peterZhi time:2020/1/3
import time
temp=time.time()
mytime=int(temp)
years=mytime//(3600*24*30*12) #年数
temp=mytime-years*3600*24*30*12
months=temp//(3600*24*30) #月份
temp=temp-months*3600*24*30
days=temp//(3600*24) #天数
temp=temp-days*3600*24
hours=temp//3600 #小时
temp=temp-hours*3600
mins=temp//60 #分钟
seconds=temp-mins*60 #秒数


print("自从1970到现在过去了",
      years,"年",
      months,"月",
      days,"日",
      hours,"时",
      mins,"分",
      seconds,"秒")
