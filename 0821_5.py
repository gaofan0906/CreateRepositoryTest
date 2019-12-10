# 最小的k个数
# 输入n个整数，找出其中最小的K个数。
# 例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。



# -*- coding:utf-8 -*-
# class Solution:
#     def GetLeastNumbers_Solution(self, tinput, k):
#         if k>len(tinput):
#             return []
#
#         sort=sorted(tinput)
#         # l=[]
#         return sort[:k]
#         # for i in range(k):
#         #     l.append(sort[i])
#         # return l

        # write code here
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        # 4.冒泡排序
        if tinput == [] or k > len(tinput):
            return []
        return self.bubble_sort(tinput)[:k]

    def bubble_sort(self, array):
        # 逆序循环
        for i in range(len(array)-1, 0, -1):
            for j in range(i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array



if __name__ == '__main__':
    s = Solution()
    str = [4,5,1,6,2,7,3,8]
    k=4
    print(s.GetLeastNumbers_Solution(str,k))