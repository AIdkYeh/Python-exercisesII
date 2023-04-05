# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 09:56:40 2023

@author: AIdkYeh
"""
"""
#練習：Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

❏ Requirements：
1. 預設題目會提供兩個變數 nums 列表和 target 整數
2. 請找出 nums 中兩數和為 target 值的 index 並存放在列表後印出
❏ Sample Input #1: nums = [2,7,11,15], target = 9 ← 預設初始化
❏ Sample Output #1: [0,1] ← 畫面輸出
❏ Sample Input #2: nums = [3,2,4], target = 6 ← 預設初始化
❏ Sample Output #2: [1,2] ← 畫面輸出
❏ Sample Code:
"""
nums = [3,3]
target = 6
d=[]
for i in nums:
    for j in range(nums.index(i)+1,len(nums)):
        if i + nums[j] == target:
            d=[nums.index(i),j]

print(d) # [0,1]

# On LeetCode Q1

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            for j in range(nums.index(i)+1,len(nums)):
                if i + nums[j] == target:
                    return [nums.index(i),j]