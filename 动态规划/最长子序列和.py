# 最大子序列和
# 动态规划
# 0923
# 在线算法，联机算法
# 一个子序列必然是以正数开头的，因为如果以负数开头，那么去掉这个子序列，那得到一个更优解。
# 一个子序列，如果一旦他的前若干个数字组成的新的个数更少的子序列的和为负数，那么去掉这个子序列，便能得到了一个更优解。
def online_algorithm(lst):
    length = len(lst)
    this_sum = max_sum = 0
    for i in range(length):
        this_sum += lst[i]
        if this_sum > max_sum:
            max_sum = this_sum
        elif this_sum < 0:
            this_sum = 0
    return max_sum


A = [6,-3,-2,7,-15,1,2,2]
print(online_algorithm(A))

# 穷举1
# 穷举所有的可能解，比较返回最优解

# def qiongju1(lst):
#     l=len(lst)
#     this_sum=max_sum=0
#     # 第一层循环的索引i表示子序列左端的位置
#     for i in range(l):
#         # 第二层循环表示子列右端位置
#         for j in range(i,l):
#             this_sum=0
#             # 第三层循环计算该子列的大小
#             for k in range(i,j):
#                 this_sum+=lst[k]
#             if this_sum>max_sum:
#                 max_sum=this_sum
#     return max_sum
#
# A = [2, 3, 4, 1, -1, 7, -3, 7, -6]
# print(qiongju1(A))

# def qiongju2(lst):
#     l=len(lst)
#     this_sum=max_sum=0
#     # 第一层循环的索引i表示子序列左端的位置
#     for i in range(l):
#         this_sum = 0
#         # 第二层循环表示子列右端位置
#         # 去掉重复计算子序列的循环，只保留循环中最大的结果
#         for j in range(i,l):
#             this_sum += lst[j]
#             if this_sum > max_sum:
#                 max_sum = this_sum
#
#     return max_sum
#
# A = [2, 3, 4, 1, -1, 7, -3, 7, -6]
# print(qiongju2(A))

# 分治法
# def divide_and_conquer(lst, left, right):
#     if left == right:
#         if lst[left] > 0:
#             return lst[left]
#         else:
#             return 0
#
#     center = (left + right) // 2
#     # 左边界最大子序列和右边界最大子序列
#     max_left_sum = divide_and_conquer(lst, left, center)
#     max_right_sum = divide_and_conquer(lst, center + 1, right)
#
#     max_left_border_sum = left_border_sum = 0
#     for i in range(center, left -1, -1):
#         left_border_sum += lst[i]
#         if left_border_sum > max_left_border_sum:
#             max_left_border_sum = left_border_sum
#
#     max_right_border_sum = right_border_sum = 0
#     for i in range(center + 1, right + 1):
#         right_border_sum += lst[i]
#         if right_border_sum > max_right_border_sum:
#             max_right_border_sum = right_border_sum
#
#     # 左、右与跨越边界的子序列
#     return max(max_left_sum, max_right_sum, max_left_border_sum + max_right_border_sum)