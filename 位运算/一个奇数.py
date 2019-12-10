# 输入数组个数
# 以空格分开创建数组
# 创建字典记录数字出现的次数
# 输出其中出现奇数次的数字
#0915
# 数组中出现奇数次的数字
# 只有一个数出现奇数次
#
# def FindNumsAppearOdd(array):
#     dict = {}
#     for i in array:
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     for k, v in dict.items():
#         if not (v % 2) == 0:
#             return k
#
#
# if __name__ == '__main__':
#     n = int(input())
#     nums = list(map(int, input().split()))
#     print(FindNumsAppearOdd(nums))

# 异或操作666
# 异或：不一样的输出1，一样的输出0
def print_odd_times_num1(arr):
    odd = 0
    for i in arr:
        odd ^= i
    return odd


if __name__ == '__main__':
    k = [3, 1, 3, 1, 2]
    print(print_odd_times_num1(k))
