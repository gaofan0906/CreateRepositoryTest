# 两个链表的第一个公共节点
# 两个链表分别压入两个栈中，然后弹出，直到弹出不相等的即为第一个公共的节点，break

# 结点类
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 链表类
class LinkedList(object):
    def __init__(self):
        self.head = None

    def creat_list_tail(self, data):
        self.head = ListNode(data[0])
        p = self.head
        # 循环插入其他节点
        for num in data[1:]:
            node = ListNode(num)
            p.next = node
            p = node

    def traveList(self):
        p = self.head
        while p:
            print(p.val)
            p = p.next


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # 创建两个栈
        stack1 = []
        stack2 = []
        # 分别将两个练链表放入
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        node1 = None
        # 倒着弹出栈内元素，直到不相等的元素输出
        while stack1 and stack2 and stack1[-1] is stack2[-1]:
            node1 = stack1.pop()
            stack2.pop()
        return node1
        # 巧妙的解法
        # 若链表长度不同，巧妙利用差值
        # 如果两个链表长度一样，则正常遍历，找到相同的或者不存在。
        # 如果两个链表长度不同，则首先短的遍历结束后会从另一个链表开头开始遍历，而当另一个节点遍历结束后从另一个链表头开始遍历时，这两个链表的差则会消除。
        # if pHead1 == None or pHead2 == None:
        #     return None
        # p1, p2 = pHead1, pHead2
        # while p1 != p2:
        #     p1 = p1.next if p1 != None else pHead2
        #     p2 = p2.next if p2 != None else pHead1
        # return p1



if __name__ == '__main__':
    s = Solution()
    l1 = LinkedList()
    l2 = LinkedList()
    # 创建两个链表
    number1 = [8, 4, 5, 7, 1, 3, 6, 2]
    number2 = [7, 3, 4, 6, 1, 3, 6, 2]
    l1.creat_list_tail(number1)
    l2.creat_list_tail(number2)
    p = l1.phead
    print(p)
    # s1.traveList()
    # s2.traveList()
    # 传递两个链表的表头节点
    # print(s.FindFirstCommonNode(l1.head, l2.head))
