# 数组中次数出现一半的数字


# 循环数组，记录每个数字出现的次数
# 字典创建，数组中的数字和出现次数
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        my_dict = dict.fromkeys(numbers, 0)
        for i in numbers:
            if i in my_dict.keys():
                my_dict[i] += 1
        l = len(numbers) >> 1

        # 如果没有符合条件的数，要返回0

        res1 = [k for k, v in my_dict.items() if v > l]

        if res1:
            return res1
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    str = [1, 2, 3, 2, 5, 4, 2]
    print(s.MoreThanHalfNum_Solution(str))
