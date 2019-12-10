# 数组中重复的数字

# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        numbers=sorted(numbers)
        for i in range(1,len(numbers)):
            if numbers[i]==numbers[i-1]:
                duplication[0]=numbers[i]
                return True
        return False

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        dict={}
        for i in numbers:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for k,v in dict.items():
            if v>1:
                duplication[0]=k
                return True
        return False

# 对数组排序
# 排序的过程中找出重复数字
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[numbers[i]] == numbers[i]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]
        return False
