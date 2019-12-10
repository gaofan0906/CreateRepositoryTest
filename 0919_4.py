# import itertools
#
# for i in itertools.permutations('abcd',4):
#     print(''.join(i))
#
#
# def perm(l):
#     if(len(l)<=1):
#         return [l]
#     r=[]
#     for i in range(len(l)):
#         s=l[:i]+l[i+1:]
#         p=perm(s)
#         for x in p:
#             r.append(l[i:i+1]+x)
#     return r
#
# # python
# # 仅通过85%
# def Permutation(ss):
#     res = []
#     if len(ss) < 2:
#         return ss
#     for i in range(len(ss)):
#         for n in map(lambda x: x+ ss[i], Permutation(ss[:i]+ss[i+1:])):
#             if n not in res:
#                 res.append(n)
#     return sorted(res)
# 循环太多，算法复杂度太大
# 85%
import itertools
def Permutation(ss,n):
    temp=[]
    for i in itertools.permutations(ss,n):
        temp.append(''.join(i))
    print(temp)
    return temp


if __name__ == '__main__':
    # n = int(input())
    # tmp = []
    # for i in range(n):
    #     s = input()
    #     tmp.append(s)
    n=5
    tmp=["ABC", "ACB", "BAC", "CAB", "CBA"]
    ss = tmp[0]
    l=len(ss)
    res = Permutation(ss,l)
    num=[i for i in res if i not in tmp]
    print(num[0])
    # for i in res:
    #     if i not in tmp:
    #         print(i)