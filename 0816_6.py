# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):

        '''
        # 循环相乘，效率低，没考虑错误用例
        result=1
        for i in range(exponent):
            result*=base
        return result'''

        '''        
        # 考虑效率
        if exponent==0:
            return 1
        if exponent==1:
            return base
        result=self.Power(base,exponent>>1) # 右移一位相当于/2
        # exponent为偶数
        result*=result
        # exponent为奇数，用这种方式来判断奇偶
        if exponent&1==1:
            result*=base
        return result'''

        # 考虑效率，考虑指数为负数
        # 设置一个指数是否小于0的标志，什么作用？
        # flag = False
        if base == 0 and exponent < 0:
            # flag = True
            return 0
        absexponent = exponent
        if exponent < 0:
            absexponent = -exponent
        # 如果指数为正，正常计算并在最后返回
        # 如果指数为负数，先取绝对值，按照正数计算完之后，输出结果返回倒数
        result = self.PowerWithUnsignedExponent(base, absexponent)

        if exponent < 0:
            # 指数为负数，计算结果返回倒数
            result = 1 / result
        return result

    # 不考虑负值的纯计算
    def PowerWithUnsignedExponent(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        result = self.PowerWithUnsignedExponent(base, exponent >> 1)  # 右移一位相当于/2
        # exponent为偶数
        result *= result
        # exponent为奇数，用这种方式来判断奇偶
        if exponent & 1 == 1:
            result *= base
        return result

        # write code here


def main():
    # 怎么自己写测试
    s = Solution()
    # flag = False
    print(s.Power(2, -2))


if __name__ == "__main__":
    main()
