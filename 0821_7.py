class Solution:
    def NumberOf1BetweenXAndN_Solution(self, n, x):
        mult, sumTimes = 1, 0
        while n//mult > 0:
            high, mod = divmod(n, mult*10)
            curNum, low = divmod(mod, mult)
            if curNum > x:
                sumTimes += high*mult + mult
            elif curNum == x:
                sumTimes += high*mult + low + 1
            else:
                sumTimes += high*mult
            mult = mult*10
        return sumTimes

if __name__ == '__main__':
    s = Solution()

    print(s.NumberOf1BetweenXAndN_Solution(100,8))

def NumberOf1Between1AndN_Solution(self, n):
    mult, sumTimes = 1, 0
    while n//mult > 0:
        high, mod = divmod(n, mult*10)
        curNum, low = divmod(mod, mult)
        if curNum > 1:
            sumTimes += high*mult + mult
        elif curNum == 1:
            sumTimes += high*mult + low + 1
        else:
            sumTimes += high*mult
        mult = mult*10
    return sumTimes