# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # 先序遍历的第一个节点是根节点,创建二叉树的根节点
        while pre:
            root = TreeNode(pre[0])
            # 找到根节点在中序中的位置
            rootid = tin.index(root.val)
            # 将中序遍历分为左右子树再递归处理
            # 递归循环把树建好了
            root.left = self.reConstructBinaryTree(pre[1:1 + rootid], tin[:rootid])
            root.right = self.reConstructBinaryTree(pre[1 + rootid:], tin[rootid + 1:])
            # 返回的是树的根节点
            return root

    def travel(self,root):
        my_queue=[]
        re_queue=[]
        my_queue.append(root)
        while my_queue:
            cur_node=my_queue.pop(0)
            re_queue.append(cur_node)
            if cur_node.left:
                my_queue.append(cur_node.left)
            if cur_node.right:
                my_queue.append(cur_node.right)
        return re_queue
def main():
    front=[1,2,4,7,3,5,6,8]
    middel=[4,7,2,1,5,3,8,6]
    tree=Solution()
    r=tree.reConstructBinaryTree(front,middel)
    print(r.val)
    print([i.val for i in tree.travel(r)])





if __name__ == "__main__":
    main()