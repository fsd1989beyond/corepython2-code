import os
import sys
import ch03.settings as sysPro
import random

# user = input('input a number:')
# print(user)

"""
book= {'title':'Python web','year':2008}
if 'year' in book:
    print("in ")
print(book.get('pub'))

#print(book['pub'])
print(book.setdefault('pub','default Value'))
print(book.keys())
print(book.values())
print(book.items())


data = (123,'abc',3.14)
for i,value in enumerate(data):
    print(i,value)

"""

# caps = {
#     '1': 'a',
#     '2': 'b',
#     '3': 'c'
# }
#
# for k, v in caps.items():
#     print(k, v)


# print(dir(sys))
# print(help(sys))

# i = 0
# while i < 11:
#    print(i)
#    i = i + 1

# for j in (0,1,2,3,4,5,6,7,8,9,10):
#    print(j)


# print(dir())
# li = [1, 2, 3, 4]
# it = iter(li)
# for x in it:
#    print(x, end="  ")

"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x
myclass = MyNumbers()
myiter = iter(myclass)


#print(next(myiter))


a = [1,2,3,4,5,7,9]
random.shuffle(a)
print(a)
a="123"
"""

# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
#
#
# # 调用printinfo 函数
# printinfo(10)
# printinfo(70, 60, 50)

# import json
# import requests
#
# gemini_ticker = 'https://api.gemini.com/v1/pubticker/{}'
# symbol = 'btcusd'
# btc_data = requests.get(gemini_ticker.format(symbol)).json()
# print(json.dumps(btc_data, indent=4))



# import matplotlib.pyplot as plt
# import pandas as pd
# import requests
#
# # 选择要获取的数据时间段
# periods = '3600'
#
# # 通过Http抓取btc历史价格数据
# resp = requests.get('https://api.cryptowat.ch/markets/gemini/btcusd/ohlc',
#   params={
#     'periods': periods
#   })
# data = resp.json()
#
# # 转换成pandas data frame
# df = pd.DataFrame(
#   data['result'][periods],
#   columns=[
#     'CloseTime',
#     'OpenPrice',
#     'HighPrice',
#     'LowPrice',
#     'ClosePrice',
#     'Volume',
#     'NA'])
#
# # 输出DataFrame的头部几行
# print(df.head())
#
# # 绘制btc价格曲线
#
#
#
# plt.show(df['ClosePrice'].plot(figsize=(14, 7)))





s = lambda x:x**2
print( s(3))