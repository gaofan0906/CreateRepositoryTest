# 二叉搜索树的后序遍历
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        l = len(sequence)
        root = sequence[l - 1]

        # 左子树节点小于根
        for i in range(l):
            if sequence[i] > root:
                break # break后会返回一个i
        for j in range(i, l):
            if sequence[j] < root:
                return False
        # 判断左子树
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        # 判断右子树
        right = True
        if i < l - 1:
            right = self.VerifySquenceOfBST(sequence[i:l - 1])
        return left and right

        # 右子树节点大于根
        # write code here
if __name__ == '__main__':
    solution = Solution()
    data = [5,7,6,9,11,10,8]
    print(solution.VerifySquenceOfBST(data))
