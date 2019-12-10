# 正负数重新排序

def sortarray(array):
    list1=[]
    list2=[]

    for i in array:
        if i<0:
            list1.append(i)
        else:
            list2.append(i)
    list3=list1+list2
    l=' '.join(str(j) for j in list3)
    return l


if __name__ == '__main__':
    n = int(input())
    num=[]
    # num=[-4,1,-5,2]
    for i in range(n):
        num.append(int(input()))
    print(sortarray(num))