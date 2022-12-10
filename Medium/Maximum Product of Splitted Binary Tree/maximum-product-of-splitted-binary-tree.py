class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        total = 0
        sub_totals = []

        def search(node):
            nonlocal total
            if node is None:
                return 0
            
            total += node.val

            subtree_val = node.val
            subtree_val += search(node.left)
            subtree_val += search(node.right)
            sub_totals.append(subtree_val)

            return subtree_val
        
        search(root)
        res = -inf

        for st in sub_totals:
            res = max(res, (total-st) * st)

        return res % (10**9 + 7)
