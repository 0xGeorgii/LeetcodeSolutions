# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if root is None:
            return []
        
        res = []
        
        def check_subtree(node, values):
            values.append(node.val)      
            if node.left is None and node.right is None:
                s = sum(values)
                if s == targetSum:
                    res.append(values)
                else:
                    return
            
            if node.left is not None:
                check_subtree(node.left, list(values))
            if node.right is not None:
                check_subtree(node.right, list(values))
            
            del values
            
        
        check_subtree(root, [])
        
        return res
