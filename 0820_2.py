# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        ret, trace = [], []
        if root:
            self.dfs(root, expectNumber, ret, trace)
        return ret

    def dfs(self, root, n, ret, trace):
        # 递归先序遍历树，把节点加入到路径中
        trace.append(root.val)
        # 若该节点是叶子节点
        if (root.left == None) and (root.right == None):
            # 比较当前路径和是否等于期待和
            if n == root.val:
                # 符合条件的一条路
                ret.append(trace[:])
        # 不是叶子节点，则接着判断左右节点
        if root.left:
            self.dfs(root.left, n - root.val, ret, trace)
        if root.right:
            self.dfs(root.right, n - root.val, ret, trace)
        # 弹出结点，每一轮递归返回到父结点时，当前路径也应该回退一个结点
        trace.pop()

    # 更加简便
    # 法2.更Python的写法
    def FindPath(self, root, expectNumber):
        def dfs(root):
            if root:
                b.append(root.val)
                if not root.left and not root.right and sum(b) == expectNumber:
                    a.append(b[:])  # 这里必须是深拷贝，所以用：
                else:
                    dfs(root.left)
                    dfs(root.right)
                b.pop()  # 弹出结点，每一轮递归返回到父结点时，当前路径也应该回退一个结点

        a, b = [], []
        dfs(root)
        return a
