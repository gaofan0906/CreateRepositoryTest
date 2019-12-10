class Node(object):
    def __init__(self, data=None, l_child=None, r_child=None):
        self.data = data
        self.l_child = l_child
        self.r_child = r_child


class B_Tree(object):
    def __init__(self, node=None):
        self.root = node

    def addnode(self, item=None):
        # 创建一个节点
        node = Node(item)
        # 如果是空树，添加到根
        if not self.root:
            self.root = node
            # print(self.root.data)
        else:
            # 不为空，按照左右顺序添加节点，构造一颗有序二叉树
            # 列表保存
            my_queue = []
            # 加入根节点
            my_queue.append(self.root)
            # 当my_queue不为空时
            while True:
                # 取出当前节点 pop移除列表的第一个元素并返回其值
                cur_node = my_queue.pop(0)
                # 如果当前节点的左孩子为空
                if not cur_node.l_child:
                    # 将节点加入当前节点的左孩子
                    cur_node.l_child = node
                    return
                # 如果当前节点的右孩子为空
                elif not cur_node.r_child:
                    # 将节点加入当前节点的右孩子
                    cur_node.r_child = node
                    return
                else:
                    # 当前节点的左右孩子都不为空，将其加入到列表中
                    my_queue.append(cur_node.l_child)
                    my_queue.append(cur_node.r_child)

    def add(self, item):
        # 创建新节点，如果是none表示空节点，后面也不会有子节点
        node = Node(data=item)
        # 如果是空树，添加到根
        # 判断是否为空树的条件
        if not self.root or self.root.data is None:
            self.root = node
        else:
            # 不是空树，左右添加节点
            my_queue = []
            my_queue.append(self.root)
            while True:
                cur_node = my_queue.pop(0)
                # 当前节点为空，跳过，占位
                if cur_node.data is None:
                    # 当前节点为空不能有子孩子
                    continue  # 继续取队列中的下一个值
                if not cur_node.l_child:
                    # 将节点加入当前节点的左孩子
                    cur_node.l_child = node
                    return
                # 如果当前节点的右孩子为空
                elif not cur_node.r_child:
                    # 将节点加入当前节点的右孩子
                    cur_node.r_child = node
                    return
                else:
                    # 当前节点的左右孩子都不为空，将其加入到列表中
                    my_queue.append(cur_node.l_child)
                    my_queue.append(cur_node.r_child)

    # 广度优先的层次遍历
    def floor_travel(self):
        # 如果是空树则直接返回一个[]
        if not self.root or self.root.data is None:
            return []
        else:
            #
            my_queue = []
            # 构造个容器来返回遍历的结果
            re_queue = []
            my_queue.append(self.root)
            while my_queue:
                # 将先进先出将队列中的元素取出
                cur_node = my_queue.pop(0)
                # 当前节点放在最终的列表中
                re_queue.append(cur_node)
                if cur_node.l_child:
                    my_queue.append(cur_node.l_child)
                if cur_node.r_child:
                    my_queue.append(cur_node.r_child)
            return re_queue

    # 前序遍历 中，左，右
    def front_travel(self):
        # 判空
        if not self.root or self.root.data is None:
            return []
        else:
            re_queue = []

            def loop(root):
                if not root:
                    return
                else:
                    # 递归
                    re_queue.append(root)
                    loop(root.l_child)
                    loop(root.r_child)

            loop(self.root)
            return re_queue

    # 中序遍历 左，中，右
    def middel_travel(self):
        # 判空
        if not self.root or self.root.data is None:
            return []
        else:
            re_queue = []

            def loop(root):
                if not root:
                    return
                else:
                    loop(root.l_child)
                    re_queue.append(root)
                    loop(root.r_child)

            loop(self.root)
            return re_queue

    # 后序遍历 左，右，中
    def back_travel(self):
        # 判空
        if not self.root or self.root.data is None:
            return []
        else:
            re_queue = []

            def loop(root):
                if not root:
                    return
                else:
                    loop(root.l_child)
                    loop(root.r_child)
                    re_queue.append(root)

            loop(self.root)
            return re_queue

    # 堆栈前序
    def front_stank_travel(self):
        # 判空
        if not self.root or self.root.data is None:
            return []
        else:
            my_stack = []
            re_queue = []
            my_stack.append(self.root)
            while my_stack:
                # 堆栈后进先出 取堆栈中的最后一个元素
                cur_node = my_stack.pop()
                re_queue.append(cur_node)
                # 如果有有孩子将它放入堆栈中
                if cur_node.r_child:
                    my_stack.append(cur_node.r_child)
                    # 左孩子放进去
                if cur_node.l_child:
                    my_stack.append(cur_node.l_child)
            return re_queue

    # 中序遍历
    def middle_stank_travel(self):
        # 判空
        if not self.root or self.root.data is None:
            return []
        else:
            my_stack = []  # 逆序存储
            re_queue = []
            temp_list = []
            my_stack.append(self.root)
            while my_stack:
                # 每次取出都当作中间节点
                cur_node = my_stack.pop()
                # 按照当前节点的右，自己，左的顺序放入栈中
                if cur_node.r_child and cur_node.r_child not in my_stack:
                    # 当前节点的右孩子先放入
                    my_stack.append(cur_node.r_child)
                if cur_node.l_child:
                    if cur_node not in temp_list:
                        # 再把自己放进去
                        my_stack.append(cur_node)
                        # 中间节点
                        temp_list.append(cur_node)
                    else:
                        re_queue.append(cur_node)
                        temp_list.remove(cur_node)
                        continue
                    # 存在左孩子，最后放入
                    my_stack.append(cur_node.l_child)
                else:
                    # 左右孩子都没有的时候就是最左边的节点，存入输出的列表中
                    re_queue.append(cur_node)
            return re_queue

    # 后序遍历
    def back_stank_travel(self):
        if not self.root or self.root.data is None:
            return []
        else:
            my_stank = []
            re_queue = []
            tmp_list = []
            my_stank.append(self.root)
            while my_stank:
                cur_node = my_stank[-1]
                # 如果是有子节点的话，就保存
                if cur_node.r_child and cur_node not in tmp_list:
                    my_stank.append(cur_node.r_child)
                if cur_node.l_child and cur_node not in tmp_list:
                    my_stank.append(cur_node.l_child)
                # 输出中间节点或者叶子节点
                if cur_node in tmp_list or (cur_node.l_child is None and cur_node.r_child is None):
                    re_queue.append(my_stank.pop())
                    if cur_node in tmp_list:
                        tmp_list.remove(cur_node)
                # 当前节点已经判断过了
                tmp_list.append(cur_node)
            return tmp_list  # re_queue


def main():
    tree = B_Tree()
    # for i in range(7):
    #     tree.addnode(i)

    for i in range(10):
        if i == 3:
            i = None
        tree.add(i)
    print([i.data for i in tree.front_stank_travel()])


if __name__ == "__main__":
    main()
