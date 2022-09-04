# #TODO need to optmize (execution time is too long)

#Tree approach
class Node:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
                
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
        root = Node(val = startPos)
        
        level = [ root ]
        
        for i in range(k):
            level_tmp = []
            for j in range(len(level)):
                n = level.pop()
                n.left = Node(val = n.val + 1)
                n.right = Node(val = n.val - 1)
                level_tmp.append(n.left)
                level_tmp.append(n.right)
            level = level_tmp
        
        res = 0
        for i in range(len(level)):
            n = level.pop()
            if n.val == endPos:
                res += 1
            
        return res

#Combinatorical approach
class _Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if startPos + k == endPos or startPos - k == endPos:
            return 1
    
        available_moves = (-1, 1)
        res = 0

        for c in itertools.product(available_moves, repeat = k):
            if startPos + sum(c) == endPos:
                res += 1
        return res
