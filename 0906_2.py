# 和为s的连续正数序列
# 牛逼的思路:滑动窗口
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # 创建一个列表存放最后的结果
        result=[]
        plow,phigh=1,2
        while phigh>plow:
            cur=((plow+phigh)*(phigh-plow+1))/2
            if cur==tsum:
                list=[]
                for i in range(plow,phigh+1):
                    list.append(i)
                result.append(list)
                plow+=1
            elif cur<tsum:
                phigh+=1
            else:
                plow+=1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.FindContinuousSequence(100))
