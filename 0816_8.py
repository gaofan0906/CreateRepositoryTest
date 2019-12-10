# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 快慢指针解决
    def FindKthToTail(self, head, k):
        # 创建两个指针
        q=m=head
        # 快指针先走k步
        for i in range(k):
            if q is None:
                return None
            q=q.next
        # 快慢指针一起走
        while q:
            q=q.next
            m=m.next
        return m


    '''    def __init__(self):
        self.head = None

    def creat_list_tail(self, data):
        self.head = ListNode(data[0])
        p = self.head
        # 循环插入其他节点
        for num in data[1:]:
            node = ListNode(num)
            p.next = node
            p = node

    # 获得链表长度
    def lenght(self):
        # if self.isEmpty():
        #     exit(0)
        p = self.head
        len = 0
        while p:
            len += 1
            p = p.next
        return len

    def FindKthToTail(self, data, k):
        p = self.head
        i = 0
        # 找到倒数第k个节点的index
        index = self.lenght() - k

        # 从头开始找下一个节点直到当前节点的index符合条件
        while p.next:
            pre = p
            p = p.next
            i += 1
            if i == index:
                return p.val

        # write code here


def main():
    # 怎么自己写测试
    data = [1, 2, 3, 4, 5]
    k=2
    l = Solution()
    l.creat_list_tail(data)
    print(l.FindKthToTail(data,k))


if __name__ == "__main__":
    main()
'''
