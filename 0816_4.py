# 矩阵覆盖
# 还是斐波那契的问题
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number==0:
            return 0
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
        # write code here


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.keep = {0:0, 1:1, 2:2}
    def rectCover(self, number):
        if number in self.keep:
            return self.keep[number]
        else:
            fn = self.rectCover(number - 1) + self.rectCover(number - 2)
            self.keep[number] = fn
            return fn

def main():
    # 怎么自己写测试
    s = Solution()
    print(s.rectCover(8))


if __name__ == "__main__":
    main()