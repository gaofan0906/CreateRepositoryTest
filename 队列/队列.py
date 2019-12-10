# 单链表实现队列
# 队列的pop=链表的popleft
# 队列的push=链表的append
# 队列先进先出

class Queue(object):
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self._item_link_list = LinkedList()

    def __len__(self):
        return len(self._item_link_list)

    def push(self,value):
        return self._item_link_list.append(value)

    def pop(self):
        if len(self)<=0:
            raise Exception('empty queue')
        return self._item_link_list.popleft()