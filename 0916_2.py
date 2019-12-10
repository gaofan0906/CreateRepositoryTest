# 翻转单词顺序
# 按照空格分割，数组翻转，再连接起来
# 先翻转整个句子，再翻转每个单词


# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # 按照空格切分，切分后成为数组


        l = list(s)
        l2 = []
        for i in l:
            if not i == '.':
                l2.append(i)
        l2 = ''.join(l2)
        print(l2)
        l3 = l2.split(' ')

        l4 = []
        for j in l3:
            if not j == '':
                l4.append(j)
        print(l4)
        print(len(l4))
        if len(l4)<1:
            return s
        # l=l[-1]
        # print(l)
        l4.append('.')
        print(l4)

        l4[0] = l4[0] + l4[-1]
        print(l4)
        l5 = []
        e = len(l4) - 2
        for j in range(e, -1, -1):
            l5.append(l4[j])
        return ' '.join(l5)
        # l3.append(l2[-1])
        # print(l3)
        # l3=l2[::-1]
        # print(l3)

    #     s = list(s)
    #     l=[]
    #     for i in range(len(s)-1):
    #         if not s[i]==s[i+1]:
    #             l.append(s[i])
    #     print(l)
    #     # 字符串全部翻转
    #     self.reverse(l, 0, len(l) - 1)
    #     l[-1]=s[0]+s[-1]
    #     print(l)
    #     # 双指针
    #     start, end = 0, 0
    #     # 分别对应前后两个空格的位置
    #     while start < len(l):
    #         # 找到第一个空格位置
    #         if l[start] == ' ':
    #             start += 1
    #             end += 1
    #         # 框定位置后，进行单词的翻转
    #         elif end == len(l) or l[end] == ' ':
    #             self.reverse(l, start, end - 1)
    #             end += 1
    #             # 翻转完成，继续下一个单词
    #             start = end
    #         else:
    #             # 找第二个空格的位置
    #             end += 1
    #     return ''.join(l)
    #
    #     # write code here
    #
    # def reverse(self, s, start, end):
    #     while start < end:
    #         s[start], s[end] = s[end], s[start]
    #         start += 1
    #         end -= 1


if __name__ == '__main__':
    s = Solution()
    str = '    '

    print(s.ReverseSentence(str))
