import pytest


# 结点类
class Node(object):
    # 结点属性：值，下一个
    def __init__(self, value=None, next=None):
        self.value = None
        self.next = next

    def __str__(self):
        """方便你打出来调试，复杂的代码可能需要断点调试"""
        return '<Node: value: {}, next={}>'.format(self.value, self.next)

    __repr__ = __str__


# 链表类
class LinkedList(object):
    # 链表属性：链表长度，root结点，tail结点
    # 初始化链表：参数为链表最大长度，如果为none，链表可以无限大
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    # 链表方法
    # 获取链表长度
    def __len__(self):
        return self.length

    # 尾插法添加结点
    def append(self, value):
        # 判断链表是否已满
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        # 新建结点
        node = Node(value)
        # 如果链表为空，将其添加到root后
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        # 链表长度加1
        self.length += 1

    # 头插法添加结点
    def appendleft(self, value):
        # 判断链表是否已满
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        # 新建结点
        node = Node(value)
        # 如果链表为空,让第一个结点作为尾结点
        if self.tailnode is None:
            self.tailnode = node
        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length += 1

    # 遍历链表
    def iter_node(self):
        # 从root的下一个结点开始遍历
        curnode = self.root.next
        # 当前结点不是尾结点
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        if curnode is not None:
            yield curnode

    # 迭代
    def __iter__(self):
        for node in self.iter_node():
            print(node.value)

    # 删除结点
    def remove(self, value):
        # 先找到值相等的结点的前一个结点，然后操作，最后删除
        # 前一个结点由root开始
        prevnode = self.root
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                # 如果当前结点是尾结点，直接让前一个结点等于尾结点即可
                if curnode is self.tailnode:
                    self.tailnode = prevnode
                del curnode
                self.length -= 1
                return 1
            else:
                prevnode = curnode
        return -1

    # 查找某一结点
    def find(self, value):
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    # 弹出头结点,按顺序删除
    def popleft(self):
        if self.root.next is None:
            raise Exception('pop from empty LinkedList!')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        # 如果是尾结点直接指向空
        if self.tailnode is headnode:
            self.tailnode = None
        del headnode
        return value

    # 清空链表
    def clear(self):
        for node in self.iter_node():
            node = None
        self.tailnode = None
        self.length = 0
        self.root = None

    # 链表翻转
    def reverse(self):
        curnode = self.root.next
        self.tailnode = curnode
        prevnode = None

        while curnode:
            nextnode = curnode.next
            curnode.next = prevnode
            if nextnode is None:
                self.root.next = curnode
            prevnode = curnode
            curnode = nextnode


def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert len(ll) == 4
    # 不明白为什么不可以
    assert ll.find(2) == 2
    assert ll.find(-1) == -1


#     assert ll.remove(0) == 1
#     assert ll.remove(10) == -1
#     assert ll.remove(2) == 1
#     assert len(ll) == 2
#     assert list(ll) == [1, 3]
#     assert ll.find(0) == -1
#
#     ll.appendleft(0)
#     assert list(ll) == [0, 1, 3]
#     assert len(ll) == 3
#
#     headvalue = ll.popleft()
#     assert headvalue == 0
#     assert len(ll) == 2
#     assert list(ll) == [1, 3]
#
#     assert ll.popleft() == 1
#     assert list(ll) == [3]
#     ll.popleft()
#     assert len(ll) == 0
#     assert ll.tailnode is None
#
#     ll.clear()
#     assert len(ll) == 0
#     assert list(ll) == []
#
#
# def test_linked_list_remove():
#     ll = LinkedList()
#     ll.append(3)
#     ll.append(4)
#     ll.append(5)
#     ll.append(6)
#     ll.append(7)
#     ll.remove(7)
#     print(list(ll))
#
#
# def test_linked_list_reverse():
#     ll = LinkedList()
#     n = 10
#     for i in range(n):
#         ll.append(i)
#     ll.reverse()
#     assert list(ll) == list(reversed(range(n)))
#
#
# def test_linked_list_append():
#     ll = LinkedList()
#     ll.appendleft(1)
#     ll.append(2)
#     assert list(ll) == [1, 2]


if __name__ == '__main__':
    test_linked_list()
    # test_linked_list_append()
    # test_linked_list_reverse()
