# 丑数
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0
        res = [1]
        t2 = t3 = t5 = 0
        nextID = 1

        while nextID < index:
            minNum = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
            res.append(minNum)

            if res[t2] * 2 <= minNum:
                t2 += 1
            if res[t3] * 3 <= minNum:
                t3 += 1
            if res[t5] * 5 <= minNum:
                t5 += 1

            nextID += 1
        return res[nextID - 1]


if __name__ == '__main__':
    s = Solution()
    # numbers=[3,32,321]

    print(s.GetUglyNumber_Solution(3))
