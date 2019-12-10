# 第一个只出现过一次的字符
# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,
# 如果没有则返回 -1（需要区分大小写）

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        if len(s)<0 or len(s)>=10000:
            return -1
        for i in s:
            if s.count(i)==1:
                return s.index(i)
                break
        return -1
        # write code here

if __name__ == '__main__':
    s = Solution()
    # numbers=[3,32,321]

    print(s.FirstNotRepeatingChar('hhelloworld'))