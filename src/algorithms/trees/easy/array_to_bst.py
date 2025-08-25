class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

    def __str__(self) -> str:
        lines = []

        def _show(node: 'TreeNode|None', prefix: str = "", is_tail: bool = True):
            if not node:
                return
            if node.right:
                _show(node.right, prefix + ("│   " if is_tail else "    "), False)
            lines.append(prefix + ("└── " if is_tail else "┌── ") + str(node.val))
            if node.left:
                _show(node.left, prefix + ("    " if is_tail else "│   "), True)

        _show(self)
        return "\n".join(lines)
    __repr__ = __str__

def sorted_array_to_bst(nums):
    l = 0
    h = len(nums) - 1

    def create_subtree(l, h):
        if (l > h): return None
        m = (h + l) // 2
        node = TreeNode(nums[m])
        node.left = create_subtree(l, m-1)
        node.right = create_subtree(m+1, h)
        return node


    return create_subtree(l, h)


if __name__ == "__main__":
    print(sorted_array_to_bst([1,2,3,4,5]))
