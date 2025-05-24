class Solution {
public:
    ListNode* sortList(ListNode* head) {
        int c =0;
        ListNode* no = head; 
        vector<int> r;
        while(no!=nullptr){
            r.push_back(no->val);
            c++;
            no = no->next;
        }
        sort(r.begin(),r.end());
        ListNode* nod = head;
        int i = 0;
        while(nod!=nullptr){
            nod->val = r[i];
            i++;
            nod = nod->next;
        }return head;
    }
};