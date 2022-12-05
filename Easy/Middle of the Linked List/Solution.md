# 💡C++ O(n) simple solution

# Intuition
Linked list does not allow us to determine its center ad hoc. Thus, we need to run through the whole list till the end once. During this tracking we need to move header accordingly **twice** slower (because we want to apper at the middle of the list `len / 2`).

# Approach
1. `p1` runs through all `ListNodes` till very end with remembering the `dist` it has passed.
2. Meanwhile, each second step `n % 2` we move `head` one step forward.
3. When `p1` reaches the end of the given list the `head` appears at the middle.

# Complexity
- Time complexity: O(n)
- Space complexity: O(1)

# Code
```
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
```
