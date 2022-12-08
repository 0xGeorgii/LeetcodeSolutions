class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def traverse_tree(root, arr):
            stack = [ root ]
            while stack:
                
                n = stack.pop()

                if n.left is not None : stack.append(n.left)
                if n.right is not None: stack.append(n.right)
                if n.left is None and n.right is None: arr.append(n.val)
        
        res1, res2 = [], []
        traverse_tree(root1, res1)
        traverse_tree(root2, res2)

        return res1 == res2
