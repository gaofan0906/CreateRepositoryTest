# 输入一个二维数组，从左到右从上到下依次增大
# 再输入一个数字，查看是否在数组中
# 输入二维数组的行数和列数
# 定义一个函数输入二维数组和整数，判断是否在里面

# 都是固定的
'''array=[[1,3,4],[6,7,9],[12,13,15]]
t=1

l1=len(array)
i=0
j=len(array[0])-1
while(i < l1 and j >= 0):
    if int(array[i][j])==t:
        print(True)
        break
    elif int(array[i][j])<t:
        i+=1
    else:
        j-=1'''

# 添加函数
'''def Find( n, array):
    l1 = len(array)
    if l1 == 0:
        return False
    else:
        i = 0
        j = len(array[0]) - 1
        while (i < l1) and (j >= 0):
            if int(array[i][j]) == n:
                return True
            elif int(array[i][j]) < n:
                i += 1
            else:
                j -= 1
    return False

array=[[1,3,4],[6,7,9],[12,13,15]]
t=10
print(Find(t,array))'''


# 添加输入
def Find( n, array):
    l1 = len(array)
    if l1 == 0:
        return False
    else:
        i = 0
        j = len(array[0]) - 1
        while (i < l1) and (j >= 0):
            if int(array[i][j]) == n:
                return True
            elif int(array[i][j]) < n:
                i += 1 # 下一行
            else:
                j -= 1 #往左边一列
    return False
# 输入一个nxn的二维数组并保存
# 矩阵的维度 输入的是字符串
n = int(input())
# 创建一个全为0的二维数组
line=[[0]*n]*n
# 循环给二维数组填值，以空格作为分割
for i in range(n):
    # 一行一行输入,保存是字符串
    line[i]=input().split(' ')

print(line)
t=int(input())
print(Find(t,line))

