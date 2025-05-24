class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head ==null || head.next == null || k ==0 ) return head;
        int l = 1;
        ListNode curr = head;
        while(curr.next != null){
            l++; curr = curr.next;
        }k = k%l;
        k = l-k;
        curr.next = head;
        while(k-- > 0) curr = curr.next;
        head = curr.next;
        curr.next = null;
        return head;
    }
}