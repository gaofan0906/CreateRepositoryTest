# 输入一个链表，反转链表后，输出新链表的表头
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # 链表判空
        if pHead==None:
            return None
        # 变量last一直都是指向pHead的上一个节点
        last=None
        # 循环反转,循环条件是pHead存在
        while pHead:
            # 先保存pHead的下一个节点
            temp=pHead.next
            # 改变了pHead.next，不太明白有什么意义
            # 让一会创建的新链表的新节点的后一节点的next节点等于当前的头结点
            # 因为在新链表中，last=pHead，所以新链表的next是相反的
            # 先让pHead.next指向新链表的当前节点
            pHead.next=last
            # 再让当前节点赋值为pHead，这样last.next就是last
            last=pHead
            pHead=temp
        return last


        # write code here