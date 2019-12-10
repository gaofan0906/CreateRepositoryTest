# 字符串排序

class Solution:
    def StrToSort(self, s):
        list_array=[]
        for i in s:
            if i is not ' ':
                s2l=list(i)
                list_array.append(s2l)
        sort_list=sorted(list_array,reverse=True)
        str_list=[]
        for j in sort_list:
            k=''.join(j)
            str_list.append(k)
        l=','.join(str_list)
        print(l)



if __name__=='__main__':
    s=Solution()
    str=input().split(',')
    s.StrToSort(str)

