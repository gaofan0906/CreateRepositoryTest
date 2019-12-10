class Solution:
    # s字符串
    def isNumeric(self, s):
        sign, decimal, hasE = False, False, False
        for i in range(0, len(s)):
            if s[i] in ['e', 'E']:
                if i == len(s) - 1 or hasE:  # e后面要有数字（e不能是字符串的最后一位），且只能出现一次
                    return False
                hasE = True
            elif s[i] == '.':  # 小数点不能出现在e后面，也不能出现2次
                if hasE or decimal:
                    return False
                decimal = True
            elif s[i] in ['+', '-']:
                if not sign and i > 0 and s[i - 1] not in ['e', 'E']:  # 第一次出现符号，但是不在开头那么要紧跟在e后面
                    return False
                if sign and s[i - 1] not in ['e', 'E']:  # 第二次出现符号只能是跟在e后面
                    return False
            else:
                if s[i] < '0' or s[i] > '9':
                    return False
        return True
