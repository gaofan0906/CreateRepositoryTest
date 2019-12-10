# 思路】借用一个辅助的栈，遍历压栈顺序，先讲第一个放入栈中，这里是1，
# 然后判断栈顶元素是不是出栈顺序的第一个元素，这里是4，很显然1≠4，所以我们继续压栈，
# 直到相等以后开始出栈，出栈一个元素，则将出栈顺序向后移动一位，直到不相等，
# 这样循环等压栈顺序遍历完成，如果辅助栈还不为空，说明弹出序列不是该栈的弹出顺序。

# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if not pushV:
            return False
        # 辅助栈
        stack=[]
        j=0
        for i in range(len(pushV)):
            stack.append(pushV[i])
            while j<len(popV) and stack[-1]==popV[j]:
                stack.pop()
                j+=1
        return stack==[]

if __name__ == '__main__':
    # 测试代码
    pushV=[1,2,3,4,5]
    popV=[4,5,3,2,1]
    solution = Solution()
    result = solution.IsPopOrder(pushV,popV)
    print(result)
