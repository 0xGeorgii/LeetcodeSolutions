class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {

        if (head == nullptr or head->next == nullptr) return head;

        auto cursor = head;

        ListNode* evenChunkHead = nullptr;
        ListNode* evenChunk = nullptr;
        ListNode* oddChunkHead = nullptr;
        ListNode* oddChunk = nullptr;
        uint i = 0;

        while (cursor)
        {
            if (i % 2 == 0)
            {
                if (evenChunk == nullptr) evenChunk = cursor;
                else
                {
                    evenChunk->next = cursor;
                    evenChunk = evenChunk->next;
                }
                if (evenChunkHead == nullptr) evenChunkHead = evenChunk;
            }
            else
            {
                if (oddChunk == nullptr) oddChunk = cursor;
                else
                {
                    oddChunk->next = cursor;
                    oddChunk = oddChunk->next;
                }
                if (oddChunkHead == nullptr) oddChunkHead = oddChunk;
            }
            
            cursor = cursor->next;
            i++;              
        }

        oddChunk->next = nullptr;
        head= evenChunkHead;
        evenChunk->next = oddChunkHead;

        return head;
    }
};
