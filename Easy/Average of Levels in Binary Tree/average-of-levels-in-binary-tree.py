class Solution:
            
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = [ ]
        nodes = [ root ]
        
        while len(nodes) > 0:
            tmp = []
            sum = 0
            cnt = 0
            while(len(nodes) > 0):
                n = nodes.pop()
                sum += n.val
                cnt += 1
                if n.left is not None:
                    tmp.append(n.left)
                if n.right is not None:
                    tmp.append(n.right)
            nodes = tmp
            res.append(sum / cnt)
        
        return res
