class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) return head;

        std::vector<int> vals;
        ListNode* x = head;

        while (x) {
            vals.push_back(x->val);
            x = x->next;
        }

        x = head;
        for (int i = vals.size() - 1; i >= 0; --i) {
            x->val = vals[i];
            x = x->next;
        }

        return head;
    }
};
