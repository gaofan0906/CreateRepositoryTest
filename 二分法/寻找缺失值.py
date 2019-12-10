# 找寻缺失值
# 尽可能的时间复杂度小，就是避免使用循环比较
# 和差相减
# def FindLostNum(array):
#     n_sum=sum(array)
#     n1=array[0]
#     n=array[-1]
#     length=len(array)
#     m_sum=(n1+n)*(length+1)//2
#
#     return m_sum-n_sum
# # num_list=list(map(int,input().split(',')))
#
# num_list=[2,3,4,5,7]
# print(FindLostNum(num_list))


# 二分查找
# 0919


# res = list(map(int, input().split(',')))

res=[0,1,3,4,5,6,7]
low,high=0,len(res)-1
while low+1<high:
    mid = int((low+high)//2)
    # 如果满足条件说明缺失数在右边
    if res[mid]==mid+res[0]:
        low=mid
    # 缺失值在左边
    elif res[mid]>mid:
        high=mid
print(high+res[0])