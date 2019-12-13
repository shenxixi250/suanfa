题目描述

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],
        3
       / \
        9  20
          /  \
         15   7
return its depth = 3.
由于树是一种递归的数据结构，因此用递归去解决的时候往往非常容易，这道题恰巧也是如此， 用递归实现的代码如下：
var maxDepth = function(root) {
    if (!root) return 0;
    if (!root.left && !root.right) return 1;
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    };

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        q, depth = [root, None], 1
        while q:
            node = q.pop(0)
            if node:
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            elif q:
                q.append(None)
                depth += 1
        return depth
加这个none是有作用的  每层结束之后都会在后面加一个none 然后depth+=1

