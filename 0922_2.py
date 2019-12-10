# 拓扑排序
# 判断有向图是否有环
import sys

''' 给定一个有向图，矩阵维数为顶点数，(i，j)表示i->j有边，求是否存在环
例：[[0, 1, 0], [0, 0, 1], [1, 0, 0]]——print(1)
[[0, 0, 0, 1, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], 
[0, 0, 0, 0, 0], [0, 1, 0, 0, 0]]——print(0)
'''
for line in sys.stdin:
    lines = eval(line)
    if len(lines) < 2:
        print(0)
    mat_i = [0] * len(lines)
    mat_o = [0] * len(lines)
    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines[i][j]:
                mat_i[j] += 1
                mat_o[i] += 1

    while (1):
        flag = 0
        for i in range(len(lines)):
            if mat_i[i] == 0 and mat_o[i] != 0:
                for j in range(len(lines)):
                    if lines[i][j]:
                        mat_i[j] -= 1
                mat_o[i] = 0
                flag = 1
        if flag == 0:
            break
    if any(mat_i):
        print(1)
    else:
        print(0)


n=int(input())




