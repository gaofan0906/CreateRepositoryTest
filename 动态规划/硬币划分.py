# 硬币划分
# 每种硬币不限次数
# 动态规划
# 0919
# 二维数组实现
# def change(coins, n):
#     # 创建二维数组
#     l = len(coins)
#     ll = l + 1
#     # 硬币种类数+1=列数数，
#     d = [[0] * ll for _ in range(n+1)]
#     # 初始化
#     for i in range(l):
#         d[i][0] = 1
#     # 循环
#     for j in range(1, l + 1):
#         for sum in range(1, n + 1):
#             d[j][sum] = 0
#             for k in range(sum // coins[j - 1]):
#                 d[j][sum] += d[j - 1][sum - k * coins[j - 1]]
#     print(d[coins.length][n])
#
#
# coins = [1, 2, 5, 10]
# n = 20
# change(coins, n)


# 简化的一维数组
def change(coins, n):
    len1 = len(coins)
    if len1 == 0 and n < 1 or n > 100000:
        return None
    # 初始化一个n+1的一位数组
    ways = [0] * (n + 1)  # 初始化
    ways[0] = 1
    for i in range(len1):
        for j in range(coins[i], n + 1):
            # 保证n小于等于100000，为了防止溢出，请将答案Mod 1000000007
            ways[j] = (ways[j] + ways[j - coins[i]]) % 1000000007
    return ways[n]


if __name__ == '__main__':
    coins, n = [1, 2, 5, 10], int(input())
    print(change(coins, n))
