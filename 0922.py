# 重复的数字
# 字典
def repeat(array):
    dict = {}
    for i in array:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for k, v in dict.items():
        if  v > 1:
            return k
if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split(' ')))
    print(repeat(nums))