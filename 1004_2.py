# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # 如果都为空，返回true
        if len(s) == 0 and len(pattern) == 0:
            return True
        # 如果pattern为空
        if len(s) > 0 and len(pattern) == 0:
            return False
        # 均不为空，且第一个字符为*
        if len(pattern) > 1 and pattern[1] == '*':
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s, pattern[:2]) or self.match(s[1:], pattern)
            else:
                return self.match(s,pattern[2:])
        if len(s)>0 and (s[0]==pattern[0] or pattern[0]=='.'):
            return self.match(s[1:],pattern[1:])
        else:
            return False
