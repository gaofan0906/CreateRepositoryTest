# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        if not A:
            return []
        num=len(A)
        B=[None]*num
        B[0]=1
        for i in range(1,num):
            B[i]=B[i-1]*A[i-1]
        temp=1
        for i in range(num-2,-1,-1):
            temp*=A[i+1]
            B[i]*=temp
        return B