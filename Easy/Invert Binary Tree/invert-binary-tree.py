# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None: return root

        q = deque([root])

        while q:
            lvl = deque([])
            while q:
                n = q.popleft()
                
                l = n.left
                r = n.right

                n.left = r
                n.right = l

                if n.left is not None: lvl.append(n.left)
                if n.right is not None: lvl.append(n.right)
                
            q = lvl
        
        return root
