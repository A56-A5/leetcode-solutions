class Solution(object):
    def insertionSortList(self, head):
        new = ListNode(0,head)
        prev,this = head,head.next
        while this:  
            if this.val >= prev.val:
                prev,this = this,this.next
                continue
            temp = new
            while this.val > temp.next.val:
                temp = temp.next
            prev.next = this.next
            this.next = temp.next
            temp.next = this
            this = prev.next
        return new.next