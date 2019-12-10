# 非递减序列
# 对于一个长度为n的整数序列，你需要检查这个序列是否可以是非递减序列，假如你最多可以改变其中的一个数。
# 非递减序列的定义是：array[i]<=array[i+1], for 1<=i<n;

num_list = list(map(int, input().split()))
count = 0
for i in range(len(num_list)):
    if i > 0:
        # 比较数组的前后两个数，记下非递减的个数
        if not num_list[i - 1] <= num_list[i]:
            count += 1
    # 非递减个数大于1，输出0
print(1 if count <= 1 else 0)