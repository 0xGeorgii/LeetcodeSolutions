/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* middleNode(struct ListNode* head){
    
    struct ListNode* p1 = head;
    struct ListNode* p2 = head;
    int cnt = 1;
    
    while(p2->next != NULL)
    {
        p2 = p2->next;
        cnt++;
    }
    
    for(int i = 0; i < cnt / 2; i++)
    {
        p1 = p1->next;
    }
    
    return p1;
}
