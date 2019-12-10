# 动态规划+滑窗

class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        n = len(grumpy)
        tmp = 0
        for i in range(n):
            if 0 == grumpy[i]:
                tmp += customers[i]
        for i in range(X):
            if 1 == grumpy[i]:
                tmp += customers[i]
        res = tmp
        for i in range(X, n):
            if 1 == grumpy[i]:
                tmp += customers[i]
            if 1 == grumpy[i - X]:
                tmp -= customers[i - X]
            res = max(res, tmp)
        return res


if __name__ == '__main__':
    s = Solution()
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    print(s.maxSatisfied(customers, grumpy, X))


def maxSatisfied(customers, grumpy, X):
    max = 0
    l = len(customers)
    # 计算初始滑窗的值，和剩下的值之和，并将其设为最大值，然后滑窗往后移一位，计算后移后的值
    for i in range(l):
        if i < X:
            max += customers[i]
        else:
            max += customers[i] * (1 - grumpy[i])
    # 滑窗
    dp = max
    for j in range(1, l - X + 1):
        dp = dp - customers[j - 1] * grumpy[j - 1] + customers[j + X - 1] * grumpy[j + X - 1]
        if dp > max:
            max = dp
    return max


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
X = 3
print(maxSatisfied(customers, grumpy, X))
