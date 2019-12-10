class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class CircularDoubleLinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.prev = node
        node.next = node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    # 尾插
    def append(self, value):
        node = Node(value=value)
        tailnode = self.tailnode() or self.root

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    # 头插
    def appendleft(self, value):
        node = Node(value=value)

        # 如果链表为空
        if self.root.next is self.root:
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node

        else:
            headnode = self.root.next
            headnode.prev = node
            node.prev = self.root
            self.root.next = node
            node.next = headnode
        self.length += 1

    def remove(self, node):
        if node is self.root:
            return
        else:
            node.prev.next=node.next
            node.next.prev=node.prev
        self.length-=1

        return node

    def iter_node(self):
        # 链表不为空
        if self.root.next is self.root:
            return
        curnode=self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode=curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        curnode=self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode=curnode.prev
        yield curnode

