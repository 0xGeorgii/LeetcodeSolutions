# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, d):            
            m = d
            if node.left is None and node.right is None:
                return m
            if node.left is not None:
                m = max(m, dfs(node.left, d+1))
            if node.right is not None:
                m = max(m, dfs(node.right, d+1))
            
            return m
        
        if root is None:
            return 0

        return dfs(root, 1)
