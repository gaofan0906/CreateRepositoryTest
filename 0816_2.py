# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
# 递归
# 跳台阶的方案数组成斐波那契数列
# 每一次选择之后剩下的台阶数又重新递归
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # 递归
        '''
        f1=1
        f2=2
        if number==1:
            return f1
        elif number==2:
            return f2
        else:
            return self.jumpFloor(number-1)+self.jumpFloor(number - 2)
        '''

        # 循环
        f1=1
        f2=2
        if number==1:
            return f1
        elif number==2:
            return f2
        else:
            while number-2>0:
                f1,f2=f2,f1+f2
                number-=1

            return f2
        # 数学模型
        # def fact(number):
        #     result = 1
        #     for i in range(1, number + 1):
        #         result *= i
        #     return result
        #
        # total = 0
        # for i in range(int(number / 2 + 1)):
        #     total += fact(i + number - 2 * i) / fact(i) / fact(number - 2 * i)
        # return total


def main():
    # 怎么自己写测试
    s = Solution()
    print(s.jumpFloor(4))


if __name__ == "__main__":
    main()
