# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        
        res = []
        parents = []
        
        while True:
            
            if root.left is not None:                  
                parents.append(root)
                root = root.left                
                continue
            
            if root.left is None:
                res.append(root.val)
            
            if root.right is not None:
                root = root.right
            else:            
                if len(parents) == 0:
                    break
                else:
                    root = parents.pop()
                    root.left = None
            
        return res
