# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = defaultdict(list)
        res[0].append((root.val, 0))
            
        level = [ (root, 0, 0) ]
        
        while len(level) > 0:
            n = level.pop()
            next_level = []            
            
            x = n[1];
            y = n[2]
            
            if n[0].left != None:
                level.append((n[0].left, x + 1, y - 1))
                res[y-1].append((n[0].left.val, x))
                
            if n[0].right != None:
                level.append((n[0].right, x + 1, y + 1))
                res[y+1].append((n[0].right.val, x))
        
        output = []
        for v in sorted(res.keys()):
            output.append(val for val, row_index in sorted(res[v], key=operator.itemgetter(1, 0)) )

        return output
