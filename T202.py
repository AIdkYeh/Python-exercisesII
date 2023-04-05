# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 09:56:40 2023

@author: AIdkYeh
"""
"""
#練習：在 Python3.9+ 版本的有一種新的字典運算「|」，可以用來將多個字典內的元素合併。那想請問你的是，在 Python3.9 版本以前，我們可以怎麼將多個字典合併成一個新的字典呢？
❏ Requirements：
1. 利用程式將多個字典內的元素合併成一個新的字典
2. 合併過程中請勿直接使用「|」運算
❏ Sample Input #1: {1:10, 2:20}、{3:30, 4:40}、{5:50, 6:60} ← 預設初始化
❏ Sample Output #1: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} ← 畫面輸出
❏ Sample Code:
"""
# #Method_1
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# d=dic1
# print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# #Method_2
# l=[]

# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5:50, 6:60}
# l.append(dic1)
# l.append(dic2)
# l.append(dic3)
# d= {}
# for i in l:
#     for j, word in i.items():
#         d.setdefault(j,word)
# print(d)

# 02
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
d = {}

'''
Your Code
'''
d = {**dic1, **dic2, **dic3}
print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}