# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        data = []
        while head is not None:
            data.append(head)
            head = head.next
        if n+1 > len(data):
            return data[0].next
        
        data[-(n+1)].next = data[-(n-1)] if n-1 > 0 else None
        
        return data[0]
