# 定义节点类
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 定义链表类
class LinkedList(object):
    def __init__(self):
        self.head = None

    # 头插法创建链表  创建出来是逆序
    # 创建链表传入啥参数啊？传入一个数组吧
    def creat_list_head(self, data):
        self.head = ListNode(data[-1])
        p = self.head
        # 循环插入其他节点
        for num in data[:-1]:
            node = ListNode(num)
            node.next = p.next
            p.next = node

    def creat_list_tail(self, data):
        self.head = ListNode(data[0])
        p = self.head
        # 循环插入其他节点
        for num in data[1:]:
            node = ListNode(num)
            p.next = node
            p = node

    def traveList(self):
        # if self.isEmpty():
        #     exit(0)
        p = self.head
        while p:
            print(p.val)
            p = p.next

    # 判断链表是否为空
    def isEmpty(self):
        if self.head.next == 0:
            return 1
        else:
            return 0

    # 返回链表长度
    def lenght(self):
        # if self.isEmpty():
        #     exit(0)
        p = self.head
        len = 0
        while p:
            len += 1
            p = p.next
        return len

    # 指定位置添加节点
    def addnode(self, value, index):
        # if self.isEmpty():
        #     exit(0)
        # if index < 0 or index > self.lenght() - 1:
        #     exit(0)
        p = self.head
        i = 0
        # 找到index前的一个节点
        while i <= index:
            pre = p
            p = p.next
            i += 1
        # 创建新节点
        node = ListNode(value)
        # 赋值
        pre.next = node
        node.next = p

    # 删除指定位置的节点
    def deletenode(self, index):
        p = self.head
        i = 0
        # 找到索引为index的节点
        while p.next:
            pre = p
            p = p.next
            i += 1
            if i == index:
                # p就是当前索引为index的节点
                pre.next = p.next
                # 删除
                p = None
                return 1
        p.next = None

if __name__ == '__main__':

    # 初始化链表与数据
    data = [1, 2, 3, 4, 5]
    l = LinkedList()
    l.creat_list_head(data) # 逆序
    # l.creat_list_tail(data)
    l.traveList()
    print('--------------------')
    l.addnode(123, 3)
    l.traveList()
    print('--------------------')
    l.deletenode(4)
    l.traveList()
