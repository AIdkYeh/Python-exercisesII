# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 09:56:40 2023

@author: AIdkYeh
"""
"""
Requirements：

1. 讓使用者輸入一個字串 s

2. 利用程式將字串中出現的 not … at all 取代成 good 後輸出（Note: 可以假設字串中最多只會出現一次 not ... at all）

❏ Sample Input #1: This company is not poor at all. ← 使用者輸入

❏ Sample Output #1: This company is good. ← 畫面輸出

❏ Sample Input #2: I'm not at all happy about it. ← 使用者輸入

❏ Sample Output #2: I'm good happy about it. ← 畫面輸出
"""

s = input() # This company is not poor at all. 
sL=s.split()
new=[]
if sL.index('at') == len(sL) - 2: # at all結尾
    for i in range(sL.index('not')):
        new.append(sL[i])
    new.append('good.')
    d=' '.join(new)
elif sL.index('at') < len(sL) - 2: # not ... at all 句中
    for i in range(sL.index('not')):
        new.append(sL[i])
    new.append('good')
    for i in range(sL.index('all')+1,len(sL)):
        new.append(sL[i])
    d=' '.join(new)
print(d) # This company is good.