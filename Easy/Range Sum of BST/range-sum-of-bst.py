class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        s = 0
        stack = [ root ]

        while stack:
            n = stack.pop()

            if low <= n.val <= high:
                s += n.val

            if n.left is not None: stack.append(n.left)
            if n.right is not None: stack.append(n.right)
        
        return s
