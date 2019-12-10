# 扑克牌顺子

# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # 先排序
        numbers.sort()
        # 统计其中0的个数
        zeros=numbers.count(0)
        # 不连续空缺
        gaps=0
        small=zeros
        big=small+1
        while big<len(numbers):
            # 有重复不可能是顺子
            if numbers[small]==numbers[big]:
                return False
            # 统计排序之后的数组中相邻数字之间的空缺总数
            gaps+=numbers[big]-numbers[small]-1
            small=big
            big+=1
        return gaps<=zeros
        # write code here

if __name__ == '__main__':
    s = Solution()
    list = [1,5,3,0,6]

    print(s.IsContinuous(list))