# 高深莫测的一道题，也是醉了
# 好难

# 采用递归的方法，假设待合并的链表1，链表2，
# 目前链表1头结点值小于链表2，则链表1的头结点为合并后链表的链表的头结点
# 则合并后的链表头节点指向的next的值为链表1的剩余节点与链表2的合并后的链表

class Solution:

    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2
    # 把list变成链表
    def getNewChart(self, list):
        if list:
            node = ListNode(list.pop(0))
            node.next = self.getNewChart(list)
            return node


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    list1 = [1, 3, 5]
    list2 = [0, 1, 4]
    testList1 = Solution().getNewChart(list1)
    testList2 = Solution().getNewChart(list2)
    final = Solution().Merge(testList1, testList2)
    while final:
        print(final.val, end=" ")
        final = final.next
