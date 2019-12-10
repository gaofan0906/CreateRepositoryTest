# 找数组中的峰值,返回位置
# 二分法
# 0923

# 直接比较
def findPeakElement(nums):
    l = len(nums)
    for i in range(l):
        # 不比较第一个和最后一个
        if i == 0 or i == l - 1:
            continue
        else:
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i
    # 没有峰值该如何返回
    # 返回了最后一个值
    if nums[0] <= nums[l - 1]:
        return l - 1
    else:
        return 0


nums = [1, 2, 3, 1]
print(findPeakElement(nums))


# 二分法
# 多个峰值返回一个即可
# 思路：如果中间元素大于其相邻后续元素，则中间元素左侧(包含该中间元素）必包含一个局部最大值。
# 如果中间元素小于其相邻后续元素，则中间元素右侧必包含一个局部最大值。
def findPeakElement(nums):
    l = len(nums)
    left = 0
    right = l - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left


nums = [1, 2, 1, 3, 4, 5, 7, 6]
print(findPeakElement(nums))
