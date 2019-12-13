
## 二叉树的定义
二叉树是每个节点最多有两个子树的树结构。通常子树被称作“左子树”（left subtree）和“右子树”（right subtree）

## 性质

性质1: 在二叉树的第i层上至多有2(i-1)个节点（i>0）
性质2: 深度为k的二叉树至多有2k - 1个节点（k>0）
性质3: 对于任意一棵二叉树，如果其叶节点数为N0，而度数为2的节点总数为N2，则N0=N2+1;
性质4: 具有n个节点的完全二叉树的深度必为 log2(n+1)
性质5: 对完全二叉树，若从上至下、从左至右编号，则编号为i的节点，其左子节点编号必为2i，其右子节点编号必为2i＋1；其父节点的编号必为i//2（i＝1 时为根,除外）


###几种特殊的树
`完全二叉树` 若设二叉树的高度为h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第h层有i## ## iijjjj
<++>
叶节点，并且叶节点都是从左到右依次排布，这就是完全二叉树。
`满二叉树` 除了叶节点外每一个节点都有左右子节点且所有叶节点都处在最底层的二叉树。
         ```
                a              a
               / \            /  \
                       b  c          b    c
              / \ / \       /  \ /  \
                      d  e         d    e f   g
         ```


## 二叉树的遍历啊

`广度优先`是  层次遍历

`深度优先`遍历三种  就是 先序 后序  中序   注意先后中 指的是根的位置  左一定是在右之前的

```py
    class Node():
        def __init__(self, item, lchild = None, rchild = None):
            self.item = item
            self.lchild = lchild 
            self.rchild = rchil
```




```python
class Tree():
    # 先定义一个带默认值None的根节点
    def __init__(self, root = None):
        self.root = root
    # 定义添加元素的方法
    def add(self, item):
        node = Node(item)
        if self.root == None:
            self.root = node
        else:
            # 注意这里是用队列的方式来循环判断当前节点有没有可加入位置的
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)
    # 定义广度优先遍历(层次遍历)方法
    def breadth_travel(self):
        if self.root == None:
            return
        else:
            # 仍然是用队列的方式实现遍历，末端按遍历顺序逐个添加节点，首端逐个弹出先读到的节点
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                print(cur.item, end = " ")
                if cur.lchild is not None:
                    queue.append(cur.lchild)
                if cur.rchild is not None:
                    queue.append(cur.rchild)
    # 定义深度优先遍历中的先序遍历
    def preorder(self, node):
        if node == None:
            return 
        else:
            print(node.item, end = " ")
            self.preorder(node.lchild)
            self.preorder(node.rchild)
    def pre_order_non_recursive(self, node):
    """借助栈实现前驱遍历
	if node == None:
	    return
	stack = []
	while node or len(stack) > 0:
	    if node:
		stack.append(node)
		print(node.item, end=' ')
		node = node.lchild
	    else:
		node = stack[-1]
		stack.pop()
		node = node.rchild
    # 定义深度优先遍历中的中序遍历
    def inorder(self, node):
        if node == None:
            return
        else:
            self.inorder(node.lchild)
            print(node.item, end = " ")
            self.inorder(node.rchild)
    def mid_order_non_recursive(self, node):
        """借助栈实现中序遍历
        if node == None:
            return
        stack = []
        while node or len(stack) > 0:
            if node:
                stack.append(node)
                node = node.lchild
            else:
                node = stack.pop()
                print(node.item, end=' ')
                node = node.rchild
    # 定义深度优先遍历中的后序遍历
    def postorder(self, node):
        if node == None:
            return
        else:
            self.postorder(node.lchild)
            self.postorder(node.rchild)
            print(node.item, end = " ")
    # 非递归算法
    e 非递归算法
    def (self, node):
        """借助两个栈实现后序遍历
        """
        if node == None:
            return
        stack1 = []
        stack2 = []
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.lchild:
					stack1.append(node.lchild)
            if node.rchild:
                stack1.append(node.rchild)
            stack2.append(node)
        while stack2:
            print(stack2.pop().item, end=' ')
        return

    # ----------- 前序遍历序列、中序遍历序列 —> 重构二叉树 ------------
    def tree_by_pre_mid(self, pre, mid):
        if len(pre) != len(mid) or len(pre) == 0 or len(mid) == 0:
            return
        T = NodeTree(pre[0])
        index = mid.index(pre[0])
        T.lchild = self.tree_by_pre_mid(pre[1:index + 1], mid[:index])
        T.rchild = self.tree_by_pre_mid(pre[index + 1:], mid[index + 1:])
        return T

    # ----------- 后序遍历序列、中序遍历序列 —> 重构二叉树 ------------
    def tree_by_post_mid(self, post, mid):
        if len(post) != len(mid) or len(post) == 0 or len(mid) == 0:
            return
        T = NodeTree(post[-1])
        index = mid.index(post[-1])
        T.lchild = self.tree_by_post_mid(post[:index], mid[:index])
        T.rchild = self.tree_by_post_mid(post[index:-1], mid[index + 1:])
        return T
	
```


```
f __name__ == "__main__":
    t = Tree()
    t.add(0)
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)
    t.breadth_travel()
    print("")
    t.preorder(t.root)
    print("")
    t.inorder(t.root)
    print("")
    t.postorder(t.root)
    print("")
```


