# 动态规划的思想
# 最长公共子串
# 0918

a, b = input().split(",")
m, n = len(a), len(b)
# 大小为n+1，m+1的二维矩阵
dp = [[0] * (n + 1) for _ in range(m + 1)]
maximum = 0
for i in range(1,m + 1):
    for j in range(1,n + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            maximum = max(maximum, dp[i][j])
print(maximum)


# 最长公共子序列
def LCS(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if string2[i - 1] == string1[j - 1]:
                res[i][j] = res[i - 1][j - 1] + 1
            else:
                res[i][j] = max(res[i - 1][j], res[i][j - 1])
    return res, res[-1][-1]


print(LCS("helloworld", "loop"))


# 最长公共子串
def LCstring(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
    result = 0
    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if string2[i - 1] == string1[j - 1]:
                res[i][j] = res[i - 1][j - 1] + 1
                result = max(result, res[i][j])
    return result

print(LCstring("helloworld","loop"))

a, b = input().split(",")
print(LCstring(a, b))

