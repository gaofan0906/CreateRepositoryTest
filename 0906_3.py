# 和为S的两个数字
# 因为数组是递增排序的，和相同的两个数，隔的越远，积越小，因此用两个指针，一个从前一个从后找，找到的第一个就是想要的最小的一组了
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        left,right=0,len(array)-1
        while left<right:
            cur=array[left]+array[right]
            if cur>tsum:
                right-=1
            elif cur<tsum:
                left+=1
            else:
                return [array[left],array[right]]
        return []

        # write code here