# 两个栈实现一个队列，实现队列的push和pop操作
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # 添加元素到stack1中
        self.stack1.append(node)
        # write code here

    def pop(self):
        # 如果stack2为空
        if not self.stack2:
            # stack1不为空
            while self.stack1:
                # 将stack1中的元素添加到stack2中
                self.stack2.append(self.stack1.pop())
            # stack2不为空直接输出
        return self.stack2.pop()
        # return xx

def main():
    # 怎么自己写测试
    s=Solution()
    # data=["PSH1","PSH2","PSH3","POP","POP","PSH4","POP","PSH5","POP","POP"]
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    s.push(4)
    print(s.pop())
    s.push(5)
    print(s.pop())
    print(s.pop())







if __name__ == "__main__":
    main()
