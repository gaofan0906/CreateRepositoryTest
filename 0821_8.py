# 把数组排成最小
# -*- coding:utf-8 -*-
class Solution:
    def theMax(self, str1, str2):

        return str1 if str1 + str2 > str2 + str1 else str2

    def PrintMinNumber(self, numbers):
        string = [str(num) for num in numbers]
        flag = True
        count = len(numbers) - 1
        while flag and count > 0:
            flag = False
            for i in range(len(numbers) - 1):
                if self.theMax(string[i], string[i + 1]) == string[i]:
                    temp = string[i]
                    del string[i]
                    string.insert(i + 1, temp)
                    flag = True
            count -= 1
        string = ''.join(string)
        return string

        # write code here
if __name__ == '__main__':
    s = Solution()
    numbers=[3,32,321]

    print(s.PrintMinNumber(numbers))