from collections import deque
# 双端队列实现栈
class Stack(object):
    def __init__(self):
        self.deque = deque()   # 你可以很容易替换为 python 内置的 collections.deque

    def push(self, value):
        self.deque.append(value)

    def pop(self):
        return self.deque.pop()


class Stack2(object):

    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def empty(self):
        return len(self._deque) == 0

# 栈溢出
# 数组实现栈