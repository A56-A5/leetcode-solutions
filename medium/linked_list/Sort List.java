class Solution {
    public ListNode sortList(ListNode head) {
        ListNode node = head;
        int l = 0;
        while(node!=null){
            l++;
            node = node.next;
        }int c =0;
        ListNode no = head; 
        int[] r = new int[l];
        while(no!=null){
            r[c] = no.val;
            c++;
            no = no.next;
        }
        Arrays.sort(r);
        ListNode nod = head;
        int i = 0;
        while(nod!=null){
            nod.val = r[i];
            i++;
            nod = nod.next;
        }return head;
    }
}