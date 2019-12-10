# # 插入排序  o(n2)
# def insertsort(array):
#     for i in range(1,len(array)):
#         key=array[i]
#         j=i-1
#         while j>0 and key<array[j]:
#             array[j+1]=array[j]
#             j-=1
#         array[j+1]=key
#
# l=[1,3,4,5,6,2,7,]
#
# insertsort(l)
#
# for i in range(0,len(l)):
#     print(l[i])

# 归并排序  O(nlogn)
def sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = sort(array[:mid])
    right = sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result += left[l:]
    result += right[r:]
    return result


l = [1, 3, 4, 5, 6, 2, 7, ]

print(sort(l))




