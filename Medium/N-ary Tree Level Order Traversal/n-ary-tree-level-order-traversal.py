"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        level = deque([root])
        res = []
        
        while len(level) > 0:
            
            tmp_level = deque()
            tmp_res = []
            
            while len(level) > 0:
                node = level.popleft()
                tmp_res.append(node.val)
                for n in node.children:                    
                    tmp_level.append(n)
                
            level = tmp_level
            res.append(tmp_res)
            
        return res

