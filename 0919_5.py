# 降水量

def trap(height):
    def stepv(num):
        temp = 0
        out = 0
        for i in num:
            if i < temp:
                out += temp
            else:
                out += i
                temp = i
        return out, temp

    height2 = height[::-1]
    v1, maxh = stepv(height)
    v2, maxh = stepv(height2)
    return v1 + v2 - len(height) * maxh - sum(height)


n = int(input())
l = list(map(int, input().split(" ")))
print(trap(l))

# 12
# 0 1 0 2 1 0 1 3 2 1 2 1