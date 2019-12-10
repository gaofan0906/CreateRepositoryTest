# 斐波那契数列
# n<=39
# 现在要求输入一个整数n，请你输出斐波那契数列的第n项
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        f0 = 0
        f1 = 1
        if n == 0:
            return f0
        elif n == 1:
            return f1
        else:
            # 循环条件是什么
            while n>0:
                # 交换
                f0,f1=f1,f0+f1
                n-=1

        return f0


def main():
    # 怎么自己写测试
    s = Solution()
    print(s.Fibonacci(10))


if __name__ == "__main__":
    main()


'''# 递归时间复杂度太大
class Solution:
    def Fibonacci(self, n):
        f0 = 0
        f1 = 1
        if n == 0:
            return f0
        elif n == 1:
            return f1
        else:
        # 递归
            return (self.Fibonacci(n - 2) + self.Fibonacci(n - 1))


def main():
    # 怎么自己写测试
    s = Solution()
    print(s.Fibonacci(10))


if __name__ == "__main__":
    main()'''

