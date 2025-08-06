class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int ans =0 ;
        struct ListNode *curr = head;
        while(curr!=nullptr){
            ans = ans<<1;
            ans = ans | curr->val;
            curr = curr->next;
        }
        return ans;
    }
};
