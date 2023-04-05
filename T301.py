# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 09:56:40 2023

@author: AIdkYeh
"""
"""
#練習：Self-Dividing Number（自除數）指的是可以被每位數的數字整除的數，
例如，128 可以同時被 1、2、8 分別整除即符合。本題請根據輸入的上下邊界，
找出該區間內的 Self-Dividing Number 中哪兩個數之間的差距最大。舉個例子，
假如從 11 - 20 符合的數有：11、12、15，其中 11 跟 12 的差距等於 1、12 跟 15 的
差距等於 3，因此差距最大是 12 跟 15。

❏ Requirements：

1. 讓使用者輸入兩個數字，代表一個區間

2. 請利用程式找出該區間中符合 Self-Dividing Number 的所有數

3. 將差距最大的 Self-Dividing Number 相鄰兩數印出

❏ Sample Input #1: 11, 20 ← 使用者輸入

❏ Sample Output #1: (12, 15) ← 畫面輸出

❏ Sample Input #2: 100, 900 ← 使用者輸入

❏ Sample Output #2: (555, 612) ← 畫面輸出

❏ Sample Code:
"""
a, b = input(), input() # 11, 20
d_list=[]
for i in range(int(a),int(b)+1):
    divide=list(map(int,list(str(i))))
    if 0 not in divide: # 除數不得為零
        ttl=0
        for j in divide:
            if i%j == 0:
                ttl+=1
        if ttl == len(divide):
            d_list.append(i)

d=()
maxi=0
for i in d_list:
    for j in range(d_list.index(i)+1,len(d_list)):
        if d_list[j]-i > maxi:
            maxi = d_list[j]-i
            d=(i, d_list[j])
        break
    
print(d) # (12, 15)