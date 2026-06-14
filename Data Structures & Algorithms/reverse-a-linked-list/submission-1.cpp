/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* curr = nullptr;
        ListNode* nxt = head;
        while(nxt != nullptr){
             ListNode* tmp = nxt->next;
             nxt->next = curr;
             curr = nxt;
             nxt = tmp;
        }
        
        return curr;
    }
};
