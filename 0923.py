# 把字符串转换成整数
class Solution:
    def StrToInt(self, s):
        res,mult,flag = 0,1,1
        if not s:
            return res
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                # 保留负号
                flag = -1
            # 去掉前面的正号
            s = s[1:]
        # 逆序循环
        for i in range(len(s)-1, -1, -1):
            tmp=s[i]
            if '9' >= s[i] >= '0':
                # 计算ASCII码，获得字符对应的整数
                res += (ord(s[i]) - 48)*mult
                mult = mult * 10
            else:
                return 0
        return res*flag
if __name__=='__main__':
    s=Solution()
    str1='+2147483647'
    str2='1a33'
    str3 = '-2147483647'
    print(s.StrToInt(str1))
    print(s.StrToInt(str2))
    print(s.StrToInt(str3))