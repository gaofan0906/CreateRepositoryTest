from collections import Counter


# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.word = []

    def FirstAppearingOnce(self):
        remm = Counter(self.word)
        for char in self.word:
            if remm[char] == 1:
                return char
        return '#'
        # write code here

    def Insert(self, char):
        self.word.append(char)
        # write code here
