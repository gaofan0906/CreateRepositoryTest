# 数组中的逆序对
# 拷贝原始数组并对原始数组进行排序
# 循环排序的数组，查看它在原数组中的位置
# -*- coding:utf-8 -*-
# class Solution:
#     def InversePairs(self, data):  # data是一个数组
#         # 新建一个数组
#         # 给定目标值，找到目标，返回索引 data.index()
#         # [0, 1, 2, 3, 4, 5, 6, 7]
#         # [1, 2, 3, 4, 5, 6, 7, 0]
#         # 我擦，时间复杂度超了
#         # 为啥 数据太大，一个for循环时间复杂度是循环的次数，data太大
#         # 咋改进，归并排序
#         new_data = sorted(data)
#         count=0
#
#         for i in new_data:
#             pos=data.index(i)
#             count+=pos
#             # 删除
#             data.pop(pos)
#         return count


# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(100000)  # 例如这里设置为十万


class Solution:
    def InversePairs(self, data):
        # write code here
        # 思路：归并排序。分为两个部分，寻找两个部分内部的逆序列，再寻找两个部分之间交叉的逆序列。
        if not data:
            return 0
        # assist中存储的是排好序的列表，它也是下一次Merge时作为参考的列表，因此除了本次迭代内的片段，其他部分也要等于原始列表
        # 由于必须保证有两个列表，两个地址，因此不能直接用assist=data
        assist = [i for i in data]
        return self.Merge(data, assist, 0, len(data) - 1) % 1000000007

    # 每一个新的递归开始时，都是要大范围重新排序的，这个范围会覆盖所有以前递归过的片段，因此data和assist可以互换，因为上一次排好序的列表只在下一次的比较时需要使用，而不需要递延到下一次的辅助列表中。
    def Merge(self, data, assist, low, high):
        # 判断终止条件：如果子部分里面只剩下1个数，此时low=high，不用比较，返回0
        if low == high:
            assist[low] = data[low]  # 由于assist和data互换了，因此如果递归到最小单位，要按照上次算出的排序方式排序
            return 0
        mid = (low + high) // 2
        left = self.Merge(assist, data, low, mid)
        print(left)
        right = self.Merge(assist, data, mid + 1, high)
        print(right)
        # 开始归并排序
        count = 0
        i = mid
        j = high
        k = high  # k为assist列表的索引
        # 从后往前进行遍历，对左子列和右子列中的数进行比较大小
        while i >= low and j > mid:
            # 如果左子列最后一个数大于右子列最后一个数，表示左子列大于右子列所有的数
            if data[i] > data[j]:
                count += j - mid  # count要加上右子列中剩下元素的个数
                assist[k] = data[i]  # 将最大的数存入辅助列表
                i -= 1  # 最大数已被排序，将左子列向前遍历一个元素
            # 如果左子列最后一个数小于等于右子列最后一个数，不构成逆序对
            else:
                assist[k] = data[j]  # 将最大的数存入辅助列表
                j -= 1  # 最大数已被排序，将右子列向前遍历一个元素
            k -= 1
        # 上面一个while中还会剩下最后一个元素没有被排序，进入assist
        while i >= low:
            assist[k] = data[i]
            i -= 1
            k -= 1
        while j > mid:
            assist[k] = data[j]
            j -= 1
            k -= 1
        return left + right + count  # 返回当前左右子列计算出的逆序对数量，加上左右子列内部的逆序对数量


if __name__ == '__main__':
    s = Solution()
    numbers = [8, 4, 5, 7, 1, 3, 6, 2]

    print(s.InversePairs(numbers))

# def merge_sort(alist):
#     if len(alist) <= 1:
#         return alist
#     # 二分分解
#     num = len(alist) // 2
#     left = merge_sort(alist[:num])
#     right = merge_sort(alist[num:])
#     # 合并
#     return merge(left, right)
#
#
# def merge(left, right):
#     '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
#     # left与right的下标指针
#     l, r = 0, 0
#     result = []
#     while l < len(left) and r < len(right):
#         if left[l] < right[r]:
#             result.append(left[l])
#             l += 1
#         else:
#             result.append(right[r])
#             r += 1
#     result += left[l:]
#     result += right[r:]
#     return result
#
#
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# sorted_alist = merge_sort(alist)
# print(sorted_alist)
