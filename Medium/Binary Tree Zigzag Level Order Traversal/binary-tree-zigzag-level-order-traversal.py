# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        res = [ [root.val] ]
        q = deque([root])
        a = 1

        while q:
            lvl = []
            while q:
                n = q.popleft()
                if n.left is not None: lvl.append(n.left)
                if n.right is not None: lvl.append(n.right)
            
            if lvl:
                if a % 2 == 0:
                    res.append([ n.val for n in lvl])
                else:
                    res.append([ n.val for n in lvl[::-1]])
            
            a += 1
            q = deque(lvl)
        
        return res
