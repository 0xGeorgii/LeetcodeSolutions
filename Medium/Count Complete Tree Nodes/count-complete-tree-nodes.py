# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        if root.left is None:
            return 1

        res, h = 0, 0        
        
        queue = deque([root])

        while queue:
            level = deque([])
            checked = False
            while queue:
                node = queue.popleft()
                if node.left is None and not checked:
                    res += len(queue) + 1
                    return res

                if not checked:
                    res += 2 ** h
                    h += 1
                    checked = True

                if node.right is not None:
                    level.append(node.right)

            queue = level

        return res
