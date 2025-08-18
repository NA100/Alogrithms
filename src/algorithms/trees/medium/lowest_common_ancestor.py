"""
Lowest Common Ancestor in a Binary Search Tree — Problem Statement
Given the root of a BST and two nodes p and q (node references), return their lowest common ancestor (LCA).
LCA definition: the deepest node that has both p and q in its subtree (a node can be a descendant of itself).
BST property: for any node x, all keys in x.left < x.val and all keys in x.right > x.val.
Assume both p and q exist in the tree.
Input / Output
Input (pointer form): root (TreeNode), p (TreeNode), q (TreeNode)
Output: TreeNode (the LCA of p and q)
Examples
Example 1
root = [6,2,8,0,4,7,9,null,null,3,5], p=2, q=8 → Output: node 6
Example 2
same tree, p=2, q=4 → Output: node 2 (ancestor case)
Example 3
root = [2,1], p=2, q=1 → Output: node 2
"""