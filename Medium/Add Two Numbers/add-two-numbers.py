# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1, n2 = "", ""

        while l1:
            n1 = str(l1.val) + n1
            l1 = l1.next
        
        while l2:
            n2 = str(l2.val) + n2
            l2 = l2.next

        r = str(int(n1) + int(n2))[::-1]
        root = ListNode(r[0])
        n = root

        for c in r[1:]:
            n.next = ListNode()
            n = n.next
            n.val = c
        
        n.val = r[-1]

        return root
