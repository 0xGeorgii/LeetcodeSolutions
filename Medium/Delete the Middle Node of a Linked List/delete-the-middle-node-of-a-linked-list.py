# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if head.next is None:
            return None
        elif head.next.next is None:
            head.next = None
            return head
        
        n1 = head
        n1_pos = 0
        
        n2 = head
        n2_pos = 0
        
        while n1.next is not None:
            n1 = n1.next
            n1_pos += 1
            if n1_pos % 2 == 0:
                while n2_pos < math.ceil(n1_pos / 2):
                    n2 = n2.next
                    n2_pos += 1
        
        while n2_pos != math.ceil(n1_pos / 2):
            n2_pos += 1
            n2 = n2.next
        
        while True:
            n2.val = n2.next.val
            if n2.next.next is None:
                n2.next = None
                break
            else:
                n2 = n2.next
        

        return head
