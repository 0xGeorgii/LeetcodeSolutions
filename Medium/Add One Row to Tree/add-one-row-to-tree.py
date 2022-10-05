# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            return TreeNode(val, root, None)
        
        level = 0
        
        nodes = deque([ root ])
        
        while len(nodes) > 0:
            tmp_nodes = deque()
            level += 1
            while len(nodes) > 0:
                node = nodes.popleft()
                if level == depth - 1:
                    
                    left = TreeNode(val, node.left if node.left is not None else None, None)
                    right = TreeNode(val, None, node.right if node.right is not None else None)
                    
                    node.left = left
                    node.right = right
                    
                else:                
                    if node.left is not None:
                        tmp_nodes.append(node.left)
                    if node.right is not None:
                        tmp_nodes.append(node.right)
            
            nodes = tmp_nodes
            
        return root
 
