# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        queue = deque([root])
        res = []
        ch = 95
        while len(queue) > 0:
            n = queue.popleft()
                
            s = f"{n.val}(l)(r)"
                                    
            if n.left is not None:
                s = s.replace("l", f"{str(hash(str(ch)))}")
                ch += 1
                queue.append(n.left)
            else:
                s = s.replace("l", "#" if n.right is not None else "")
            
            if n.right is not None:
                s = s.replace("r", f"{str(hash(str(ch)))}")
                ch += 1
                queue.append(n.right)
            else:
                s = s.replace("r", "")
                            
            res.append(s)
        
        result = res[0]
        ch1 = 95
        for i in range(1, len(res), 1):
            result = result.replace(str(hash(str(ch1))), res[i], 1)
            ch1 += 1
                    
        return result.replace("()", "").replace("#", "")
