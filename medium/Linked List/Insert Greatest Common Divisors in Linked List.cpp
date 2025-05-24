class Solution {
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if(head == nullptr || head->next == nullptr) return head;

        ListNode* prev = head;
        ListNode* curr = head->next;

        while(curr != nullptr){
            int x = gcd(prev->val,curr->val);
            ListNode* g = new ListNode(x);

            prev->next = g;
            g->next = curr;

            prev = curr;
            curr = curr->next;
        }return head;
    }
private:
    int gcd(int a,int b){
        while(b!=0){
            int temp = b;
            b = a%b;
            a = temp;
        }return a;
    }
};