# python 实现链表数据结构
# 用类的引用代替指针
# 定义节点类

# 不能用内置函数
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        s=[]
        while listNode is not None:
            s.append(listNode.val)
            listNode=listNode.next
        # 想要循环输出，但是不能逆序
        '''        
        result=[]
        for i in range(len(s)):
            result.append(s[i])
        return result'''
        # 栈的后进先出
        result=[]
        while len(s):
            result.append(s.pop())
        return result

def main():
    # 怎么自己写测试
    s = Solution()
    data=[1,2,3]

    print(s.printListFromTailToHead(1))


if __name__ == "__main__":
    main()





# 用节点类初始化一个链表
# data=[1,2,3]
# data1=ListNode(1)
# data2=ListNode(2)
# data3=ListNode(3)
# data1.next=data2
# data2.next=data3

# # 建立一个头节点
# head=ListNode(data[0])
#
# # 循环指定next
# for i in data[1:]:
#     node=ListNode(i)
#     head.next=node
#     head=head.next
#
#
# # 循环遍历
# while head:
#     print(head.next)
#     print(head.next.val)
# /usr/bin/python
# -*- coding: utf-8 -*-
# Function: simulate the link-list in python
# __author__: Tresser
#

# class LNode(object):
#     # 结点初始化函数, p 即模拟所存放的下一个结点的地址
#     # 为了方便传参, 设置 p 的默认值为 0
#     def __init__(self, data, p=0):
#         self.data = data
#         self.next = p
#
#
#
# class LinkList(object):
#     def __init__(self):
#         self.head = None
#
#     # 链表初始化函数, 方法类似于尾插
#     def initList(self, data):
#         # 创建头结点
#         self.head = LNode(data[0])
#         p = self.head
#         # 逐个为 data 内的数据创建结点, 建立链表
#         for i in data[1:]:
#             node = LNode(i)
#             p.next = node
#             p = p.next
#
#     # 链表判空
#     def isEmpty(self):
#         if self.head.next == 0:
#             print("Empty List!")
#             return 1
#         else:
#             return 0
#
#     # 取链表长度
#     def getLength(self):
#         if self.isEmpty():
#             exit(0)
#
#         p = self.head
#         len = 0
#         while p:
#             len += 1
#             p = p.next
#         return len
#
#     # 遍历链表
#     def traveList(self):
#         if self.isEmpty():
#             exit(0)
#         print('\rlink list traving result: '),
#         p = self.head
#         while p:
#             print(p.data),
#             p = p.next
#
#     # 链表插入数据函数
#     def insertElem(self, key, index):
#         if self.isEmpty():
#             exit(0)
#         if index < 0 or index > self.getLength() - 1:
#             print("\rKey Error! Program Exit.")
#             exit(0)
#
#         p = self.head
#         i = 0
#         while i <= index:
#             pre = p
#             p = p.next
#             i += 1
#
#         # 遍历找到索引值为 index 的结点后, 在其后面插入结点
#         node = LNode(key)
#         pre.next = node
#         node.next = p
#
#     # 链表删除数据函数
#     def deleteElem(self, index):
#         if self.isEmpty():
#             exit(0)
#         if index < 0 or index > self.getLength() - 1:
#             print("\rValue Error! Program Exit.")
#             exit(0)
#
#         i = 0
#         p = self.head
#         # 遍历找到索引值为 index 的结点
#         while p.next:
#             pre = p
#             p = p.next
#             i += 1
#             if i == index:
#                 pre.next = p.next
#                 p = None
#                 return 1
#
#         # p的下一个结点为空说明到了最后一个结点, 删除之即可
#         pre.next = None
#
#     # 链表增加节点
#     def add(self,num):
#         temp=self.head
#         while temp.next:
#             temp=temp.next
#         temp.next=LNode(num)
#
#
# # 初始化链表与数据
# data = [1, 2, 3, 4, 5]
# l = LinkList()
# l.initList(data)
# l.traveList()
#
# # 插入结点到索引值为3之后, 值为666
# l.insertElem(666, 3)
# l.traveList()
#
# # 删除索引值为4的结点
# l.deleteElem(4)
# l.traveList()
#
# # 新增节点
# l.add(123)
# l.traveList()
