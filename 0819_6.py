# 从上到下打印二叉树
# 利用队列的先进先出(FIFO)特性解决。
# 每从队列头部获取一个节点，就将该节点的左右子节点存入队列的尾部。如此往复，直至队列为空。
# 广度优先搜索



# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # 队列
        queue = []
        result = []
        if not root:
            return result
        queue.append(root)
        # 循环条件是队列有值
        while queue:
            cur_node = queue.pop(0)
            if cur_node == None:
                continue
            else:
                result.append(cur_node.val)
            if cur_node != None:
                queue.append(cur_node.left)
            if cur_node != None:
                queue.append(cur_node.right)
        return result

    # 给定二叉树的前序遍历和中序遍历，获得该二叉树
    def getBSTwithPreTin(self, pre, tin):
        if len(pre) == 0 | len(tin) == 0:
            return None

        root = treeNode(pre[0])
        for order, item in enumerate(tin):
            if root.val == item:
                root.left = self.getBSTwithPreTin(pre[1:order + 1], tin[:order])
                root.right = self.getBSTwithPreTin(pre[order + 1:], tin[order + 1:])
                return root


class treeNode:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


if __name__ == '__main__':
    flag = "printTreeNode"
    solution = Solution()
    preorder_seq = [1, 2, 4, 7, 3, 5, 6, 8]
    middleorder_seq = [4, 7, 2, 1, 5, 3, 8, 6]
    treeRoot1 = solution.getBSTwithPreTin(preorder_seq, middleorder_seq)
    if flag == "printTreeNode":
        newArray = solution.PrintFromTopToBottom(treeRoot1)
        print(newArray)
