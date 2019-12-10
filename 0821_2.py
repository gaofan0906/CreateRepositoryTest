# 二叉搜索树和双链表
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        left=self.Convert(pRootOfTree.left)
        p=left

        # 左子树的最右节点
        while left and p.right:
            p=p.right

        # 左子树不为空
        if left:
            p.right=pRootOfTree
            pRootOfTree.left=p

        right=self.Convert(pRootOfTree.right)

        if right:
            right.left=pRootOfTree
            pRootOfTree.right=right
        return left if left else pRootOfTree

        # write code here