# 递增数组的旋转，输出最小值
# 考虑用到递增这个特性
# 解题思路是二分查找
# 因为是递增的有一定顺序的，所以用二分查找最快
# 当中间数大于最左边的数时，min一定在右边
# 当中间数小于最左边的数时，min在左边或者就是中间数
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        s = 0
        e = len(rotateArray) - 1
        # 将m初始化为s，如果第一个数字就小于最后一个数字说明，数组有序，可以直接返回第一个数字
        # 但是题目要求不会出现这种情况，所以没必要
        # m=s
        # 循环条件可以是索引的大小比较
        # 或者数值的比较 rotateArray[s]>=rotateArray[e] 第一个指针所指向的数不会小于第二个指针的
        # while rotateArray[s]>=rotateArray[e]:
        while s < e:
            # 如果两个指针指向相邻的数的时候，即索引值相差为1的时候，后一个指针指向的就是最小的值
            if e - s == 1:
                return rotateArray[e]
            # 如果不是就计算中间值
            # 中间数每次都要重新计算
            m = int(s + (e - s) / 2)
            # 中间值大于第一个值，说明中间值在前一个递增序列，最小值在它后面
            if rotateArray[m] >= rotateArray[s]:
                s = m
            # 中间值小于等于最后一个值，说明最小值可能就是中间值或者最小值在它前面
            elif rotateArray[m] <= rotateArray[e]:
                e = m
            # 有一种特殊情况
            # s,m,e 所指向的数值大小相等
        return rotateArray[m]


def main():
    # 怎么自己写测试
    s = Solution()
    data = [3, 4, 5, 1, 1, 2]
    print(s.minNumberInRotateArray(data))


if __name__ == "__main__":
    main()

# 二分查找基本操作
'''class Solution:
    def search(self, Array,n):
        s = 0
        e = len(Array) - 1
        while s + 1 < e:
            # 防止溢出
            # m算出来是小数，怎么处理
            # int()转换
            m = int(s + (e - s) / 2)
            if Array[m]==n:
                return True
            elif Array[m]<n:
                s=m
            else:
                e=m
        return False


def main():
    # 怎么自己写测试
    s=Solution()
    data=[1,2,3,4,5,6,7,8]
    n=0
    print(s.search(data,n))



if __name__ == "__main__":
    main()'''

'''
# 自己实现没成功
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        # 找到数组中最大值的index，然后返回下一个值
        max = 0
        for i in rotateArray:
            if i > max:
                max = i
            else:
                max=max
        rotateArray.index(max)
        num = rotateArray.index(max)+1

        return rotateArray[num]


def main():
    # 怎么自己写测试
    s = Solution()
    data = [3, 4, 5, 1, 2]
    print(s.minNumberInRotateArray(data))


if __name__ == "__main__":
    main()'''
