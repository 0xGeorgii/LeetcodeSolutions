# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        def check_subtree(node, value):
            value += node.val   
            if node.left is None and node.right is None:
                return value == targetSum
            
            l, r = False, False
            
            if node.left is not None:
                l = check_subtree(node.left, value)
            if node.right is not None:
                r = check_subtree(node.right, value)
                
            return l or r
        
        return check_subtree(root, 0)
