# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def caclLeftSubTree(self, node: TreeNode):
        if node.left is None:
            return node.val
        else:
            return node.val + self.isNodeInValinSubtree(node.left)
        
    def caclRightSubTree(self, node: TreeNode):
        if node.right is None:
            return node.val
        else:
            return node.val + self.isNodeInValinSubtree(node.right)
        
    def isNodeInValinSubtree(self, node: TreeNode):
        return self.caclLeftSubTree(node) + self.caclRightSubTree(node)        
    
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque([root])
        while len(queue) > 0:
            n = queue.popleft()
            
            if n.left is not None:
                if self.isNodeInValinSubtree(n.left) > 0:
                    queue.append(n.left)
                else:
                    n.left = None

            if n.right is not None:
                if self.isNodeInValinSubtree(n.right) > 0:
                    queue.append(n.right)
                else:
                    n.right = None
        
        return None if root.val == 0 and root.left is None and root.right is None else root
