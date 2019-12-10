# 翻转单词顺序
# 按照空格分割，数组翻转，再连接起来
# 先翻转整个句子，再翻转每个单词


# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # # 按照空格切分，切分后成为数组
        # l=s.split(' ')
        # l=list(s)
        # l=''.join(l)
        # print(l)
        # l2=[]
        # for i in l:
        #     if not i=='':
        #        l2.append(i)
        #
        # l2[0]=l2[0]+l2[-1]
        # print(l2)
        # l3=[]
        # e = len(l2)-2
        # for j in range(e,-1,-1):
        #     l3.append(l2[j])
        # # l3.append(l2[-1])
        # # print(l3)
        # # l3=l2[::-1]
        # # print(l3)
        # return ''.join(l3)
        s = list(s)
        # print(s)
        # 字符串全部翻转
        self.reverse(s, 0, len(s) - 1)
        # print(s)
        # 双指针
        start, end = 0, 0
        # 分别对应前后两个空格的位置
        while start < len(s):
            # 找到第一个空格位置
            if s[start] == ' ':
                start += 1
                end += 1
            # 框定位置后，进行单词的翻转
            elif end == len(s) or s[end] == ' ':
                self.reverse(s, start, end - 1)
                end += 1
                # 翻转完成，继续下一个单词
                start = end
            else:
                # 找第二个空格的位置
                end += 1
        return ''.join(s)

        # write code here

    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


if __name__ == '__main__':

    s = Solution()
    str = "It's a dog!"

    print(s.ReverseSentence(str))
