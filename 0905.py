# 数字在排序数组中出现的次数
# 有序想到二分法
# 二分查找某个数，并记下出现的次数
# 找到重复数字最左边的位置，重复数字最右边的位置，相减
# 二分查找到给定的数字及其坐标。以该坐标为中点，向前向后找到这个数字的 始 – 终 位置。
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if len(data)<1:
            return 0
        mid = len(data)//2
        if data[mid]==k:
            start,end=mid,mid
            # 逆序循环
            for i in range(mid,-1,-1):
                if data[i]==k:
                    start-=1
            for j in range(mid+1,len(data)):
                if data[j]==k:
                    end+=1
            return end-start

            # count,mida,midz=1,mid-1,mid+1
            # # 查找左边
            # while mida>=0 and data[mida]==k:
            #     count+=1
            #     mida-=1
            # # c查找右边
            # while midz<len(data)and data[midz]==k:
            #     count+=1
            #     midz+=1
            # return count


        elif data[mid]>k:
            return self.GetNumberOfK(data[:mid],k)
        else:
            return self.GetNumberOfK(data[mid+1:],k)


if __name__ == '__main__':
    s = Solution()


"""
1. 二分查找是有条件的，首先是有序，其次因为二分查找操作的是下标，所以要求是顺序表
2. 最优时间复杂度：O(1)
3. 最坏时间复杂度：O(logn)
"""

# def binary_chop(alist, data):
#     """
#     递归解决二分查找
#     :param alist:
#     :return:
#     """
#     n = len(alist)
#     if n < 1:
#         return False
#     mid = n // 2
#     if alist[mid] > data:
#         return binary_chop(alist[0:mid], data)
#     elif alist[mid] < data:
#         return binary_chop(alist[mid+1:], data)
#     else:
#         return True

# def binary_chop(alist, data):
#     """
#     非递归解决二分查找
#     :param alist:
#     :return:
#     """
#     n = len(alist)
#     first = 0
#     last = n - 1
#     while first <= last:
#         mid = (last + first) // 2
#         if alist[mid] > data:
#             last = mid - 1
#         elif alist[mid] < data:
#             first = mid + 1
#         else:
#             return True
#     return False
#
# if __name__ == '__main__':
#     lis = [2,4, 5, 12, 14, 23]
#     if binary_chop(lis, 14):
#         print('ok')