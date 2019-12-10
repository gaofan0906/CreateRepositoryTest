# 圆圈中最后剩下的数
# 递推公式
# 数学题
# n个人，m数字
#0911
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n<1 or m<1:
            return -1
        last=0
        for i in range(2,n+1):
            last=(last+m)%i
        return last

# 每次删除的数的小标为(m-1)%len(num)，删除一个后，则后面的节点变成了头节点
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n<=0:
            return -1#判断异常输入
        num = list(range(n))
        while len(num)>1:
            lucky = (m-1)%len(num)
            num = num[lucky+1:]+num[:lucky]
        return num[0]
if __name__ == '__main__':
    s = Solution()
    print(s.LastRemaining_Solution(5,3))