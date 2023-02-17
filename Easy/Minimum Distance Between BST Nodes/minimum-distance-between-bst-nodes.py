# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        s = set()

        def dfs(node):
            s.add(node.val)
            if node.left is not None: dfs(node.left)            
            if node.right is not None: dfs(node.right)

        dfs(root)
        s = list(s)
        s.sort()
        res = inf
        for i in range(1, len(s)):
            res = min(res, abs(s[i-1] - s[i]))
        
        return res
