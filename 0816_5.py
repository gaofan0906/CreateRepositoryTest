# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        # 负数取补码
        if n < 0:
            n = n & 0xffffffff
        count = 0  # 用来记录二进制中1的个数
        # n>0,在循环中，n一直会改变
        while n:
            # 消去n最后一位上的1，消除几次就有几个1
            # 7&6=6 0111&0110=0110
            # 6&5=4 0110&0101=0100
            # 4&3=0 0100&0011=0000
            n = n & (n - 1)
            count += 1
            # 1001&0001 最后一位做与运算
            # if n & 1: # 返回的结果不是1或者0吗，这样也是可以判断的吗
            #     # 总数+1
            #     count += 1
            # # 右移动运算符：右移一位
            # n = n >> 1
        return count


def main():
    # 怎么自己写测试
    s = Solution()
    print(s.NumberOf1(7))


if __name__ == "__main__":
    main()
