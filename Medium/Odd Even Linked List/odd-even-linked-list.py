class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None: return head

        cursor = head
        even_chunk_head = None
        even_chunk = None
        odd_chunk_head = None
        odd_chunk = None
        i = 1

        while cursor is not None:

            if i % 2 == 1:            
                if even_chunk is None:
                    even_chunk = cursor
                else:
                    even_chunk.next = cursor
                    even_chunk = even_chunk.next
                if even_chunk_head is None:
                    even_chunk_head = even_chunk                
            else:
                if odd_chunk is None:
                    odd_chunk = cursor
                else:
                    odd_chunk.next = cursor
                    odd_chunk = odd_chunk.next
                if odd_chunk_head is None:
                    odd_chunk_head = odd_chunk

            cursor = cursor.next
            i += 1


        odd_chunk.next = None
        head = even_chunk_head
        even_chunk.next = odd_chunk_head
        return head
