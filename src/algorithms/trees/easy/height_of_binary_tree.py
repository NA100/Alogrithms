"""
For maxDepth on a binary tree:
Time Complexity (DFS or BFS): O(n) — every node is visited exactly once.

Space Complexity:
Recursive DFS: O(h) call stack, where h is tree height.
Balanced tree: O(log n)
Skewed tree: O(n)
Iterative BFS: O(w) for the queue, where w is the tree’s maximum width.
Worst case (near-complete tree): O(n) (since the widest level can hold ~n/2 nodes)
"""
from collections import deque

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def maxDepth_recursive(node):
    if not node:
        return 0
    else:
        return 1 + max(maxDepth(node.left), maxDepth(node.right))

def maxDepth_iterative(node):
    q = deque([node])
    depth = 0
    while q:
        depth += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return depth



def main():
     root = TreeNode(3,
                TreeNode(9),
                TreeNode(20, TreeNode(15), TreeNode(7))
        )
     print(maxDepth_iterative(root))

if __name__ == "__main__":
    main()