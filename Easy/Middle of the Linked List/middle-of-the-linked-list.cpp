class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        
        auto p1 = head;
        uint dist = 0;

        while (p1)
        {
            p1 = p1->next;
            dist++;
            if (dist % 2 == 0)
            {
                head = head->next;
            }
        }

        return head;

    }
};
