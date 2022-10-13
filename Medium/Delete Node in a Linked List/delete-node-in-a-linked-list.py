class Solution:
    def deleteNode(self, node):
        
        while True:
            node.val = node.next.val
            if node.next.next is None:
                node.next = None
                break
            else:
                node = node.next
