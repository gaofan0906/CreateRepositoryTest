# 树的子结构
# 递归
# 判断是否是子结构的时候，如果当前值相等，需要进行左右值是否相等的判断；如果当前值不等，则判断Root1的左右子树是否包含Root2.
# 空值判读
# 是否是子树的函数，递归用


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        # 空树不是子结构
        if pRoot1 == None or pRoot2 == None:
            return False
        return self.isSubtree(pRoot1, pRoot2)

    def isSubtree(self, p1, p2):
        # p2比较完了还没有返回flase说明存在子树
        if p2 == None:
            return True
        # p1为空，p2不为空，说明没有找到
        if p1 == None:
            return p1 == p2
        res = False
        # 当前值相等
        if p1.val == p2.val:
            # 接着判断左右值是否相等
            res = self.isSubtree(p1.left, p2.left) and self.isSubtree(p1.right, p2.right)
        # 不等，则判断p1的左右子树是否包含p2
        return res or self.isSubtree(p1.left, p2) or self.isSubtree(p1.right, p2)
