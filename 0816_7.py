# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # 循环检查是否是偶数或者奇数
        odd=[]
        even=[]
        for i in array:
            # 如果是奇数，就拿出来保存
            if i&1==1:
                odd.append(i)
            else:
                even.append(i)
        result=odd+even
        return result


def main():
    # 怎么自己写测试
    s = Solution()
    data=[1,2,3,4,5,6,7,8]
    print(s.reOrderArray(data))


if __name__ == "__main__":
    main()

