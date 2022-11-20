# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        sl = []
        
        stack = [ root ]
        
        while True:
            
            n = stack.pop()
            bisect.insort(sl, n.val)
            
            if n.left is not None:
                stack.append(n.left)
            if n.right is not None:
                stack.append(n.right)
            
            if len(stack) == 0:
                break
        
        res = []

        for q in queries:
            i = bisect.bisect_left(sl, q)
            
            if i == len(sl):
                res.append(
                    (sl[-1], -1)
                )
            elif sl[i] == q:
                res.append(
                    (q, q)
                )
            elif i == 0:
                res.append(
                    (-1, sl[i])
                )
            else:
                res.append(
                    (sl[i-1], sl[i])
                )
        

        return res
