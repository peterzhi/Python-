# ！/usr/bin/env python 
# -*- coding:utf-8 -*-
# author: peterZhi time:2020/1/3
#贷款计算
#输入月息、贷款金额、还款年限，运行后输出月供以及总还款金额。
#月供= (贷款金额 x 月利率) / (1- [ 1/ (1+月利率)^(年限x12) ] )
#总还款金额= 月供 x 年限 x 12

year=eval(input("请输入贷款年限:"))
money=eval(input("请输入贷款金额:"))
rate=eval(input("请输入月息:"))

Mthmoney= (money * rate) / (1- (1/ (1+ rate)**(year* 12) ) )
SumMoney= Mthmoney*year*12
print("月供为:",int(Mthmoney),"元/月")
print("年利息为:",int((SumMoney-money)/year),"元/年")
print("年还款金额为:",int(Mthmoney*12),"元/年")
print("总利息为:",int(SumMoney-money),"元")
print("总还款金额为:",int(SumMoney),"元")
