class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;

        ArrayList<Integer> list = new ArrayList<>();
        ListNode x = head;

        while (x != null) {
            list.add(x.val);
            x = x.next;
        }

        x = head;
        int i = list.size() - 1;
        while (x != null) {
            x.val = list.get(i--);
            x = x.next;
        }

        return head;
    }
}
