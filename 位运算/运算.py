# 不用加减乘除做加法
# 位运算
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        while num2:
            sum=num1^num2
            carry=0xFFFFFFFF&(num1 & num2)<<1
            carry = -(~(carry - 1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
            num1 = sum
            num2 = carry
        return num1
        # write code here

# 短路特性
# 不使用加减乘除做运算
# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        result=n
        temp=n>0 and self.Sum_Solution(n-1)
        result=result+temp
        return result
        # write code here

if __name__ == '__main__':
    s = Solution()
    # list = [1,5,3,0,6]

    print(s.Sum_Solution(5))