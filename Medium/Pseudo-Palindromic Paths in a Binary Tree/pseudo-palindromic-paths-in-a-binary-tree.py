# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildPath(self, node, chain):
        if node.left is None and node.right is None:
            chain[node.val - 1] += 1
            return 1 if len(list(filter(lambda x: x % 2,chain))) <= 1 else 0
        
        chain[node.val - 1] += 1
        res = 0
        
        if node.left is not None:
            res += self.buildPath(node.left, list(chain))
        if node.right is not None:
            res += self.buildPath(node.right, list(chain))
            
        return res
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return self.buildPath(root, [0] * 9)
