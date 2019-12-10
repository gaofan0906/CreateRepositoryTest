# 左旋转字符串
# 翻转实现
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        l = list(s)
        self.reverse(l, 0, n - 1)
        self.reverse(l, n, len(l) - 1)
        self.reverse(l, 0, len(l) - 1)
        return ''.join(l)

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    s = Solution()
    str = 'abcdefg'
    n = 3
    print(s.LeftRotateString(str, n))
