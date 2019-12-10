# 字符串的全排列

# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        res = []
        self.helper(ss, res, '')
        return res
        # return sorted(list(set(ss)))
        # write code here

    def helper(self, ss, res, path):
        if not ss:
            res.append(path)
        else:
            for i in range(len(ss)):
                self.helper(ss[:i] + ss[i + 1:], res, path + ss[i])

    # def Permutation(self, ss):
    #     list = []
    #     if len(ss) <= 1:
    #         return ss
    #     for i in range(len(ss)):
    #         for j in map(lambda x: ss[i]+x, self.Permutation(ss[:i]+ss[i+1:])):
    #             if j not in list:
    #                 list.append(j)
    #     return list



if __name__ == '__main__':
    s=Solution()
    str='abc'
    print(s.Permutation(str))




                                                


