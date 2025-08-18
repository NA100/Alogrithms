"""
Minimum Depth of Binary Tree — Problem Statement
Given the root of a binary tree, return its minimum depth.
Minimum depth = the number of nodes on the shortest path from the root down to the nearest leaf.
A leaf is a node with no children.
If the tree is empty, the minimum depth is 0.
"""

from collections import deque

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def min_height_iterative(node):
    if not node: return 0

    q = deque([node])
    min_height = 0

    while q:
        min_height += 1
        for _ in range(0, len(q)):
            node = q.popleft()
            if not node.left:  return min_height
            if not node.right: return  min_height
            q.append(node.left)
            q.append(node.right)

    return min_height



if __name__ == "__main__":
     root = TreeNode(3,
                TreeNode(9),
                TreeNode(20, TreeNode(15), TreeNode(7))
        )
     print(min_height_iterative(root))
