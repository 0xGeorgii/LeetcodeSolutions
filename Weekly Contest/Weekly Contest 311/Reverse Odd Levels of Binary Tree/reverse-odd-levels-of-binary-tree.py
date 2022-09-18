# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        level = deque([root])
        level_number = 1
        
        def swapNodesVal(node, node1):
            tv = node.val
            node.val = node1.val
            node1.val = tv
        
        while len(level) > 0:            
            tmp_level = deque()            
            while len(level) > 0:                
                if level_number % 2 == 0:
                    drop_queue = deque(level)
                    while len(level) > 0:                        
                        node1 = level.popleft()
                        node2 = level.pop()                        
                        swapNodesVal(node1, node2)
                    while len(drop_queue) > 0:
                        node = drop_queue.popleft()            
                        if node.left is not None:
                            tmp_level.append(node.left)
                            tmp_level.append(node.right)                        
                else:
                    node = level.popleft()            
                    if node.left is not None:
                        tmp_level.append(node.left)
                        tmp_level.append(node.right)
                    
            level_number += 1   
            level = tmp_level
        return root
