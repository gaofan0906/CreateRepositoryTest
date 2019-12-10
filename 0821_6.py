# 连续子数组的最大和
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        n = len(array)
        dp = [i for i in array]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + array[i], array[i])
        return max(dp)
        # write code here


if __name__ == '__main__':
    s = Solution()
    str = [6, -3, -2, 7, -15, 1, 2, 2]
    print(s.FindGreatestSumOfSubArray(str))
