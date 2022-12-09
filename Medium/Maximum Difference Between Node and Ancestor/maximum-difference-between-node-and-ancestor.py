# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def find_max(node, out, arr):
            arr.append(node.val)
            for v in arr:
                out = max(out, abs(v-node.val))
 
            if node.left is None and node.right is None: return out

            if node.left is not None:
                out = max(out, find_max(node.left, out, arr[:]))
            if node.right is not None:
                out = max(out, find_max(node.right, out, arr[:]))
            return out

        return find_max(root, -inf, [])

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def find_max(node, min_val, max_val):
            if node is None: return max_val - min_val

            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            l = find_max(node.left, min_val, max_val)
            r = find_max(node.right, min_val, max_val)

            return max(l, r)

        return find_max(root, root.val, root.val)
