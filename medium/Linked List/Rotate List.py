class Solution(object):
    def rotateRight(self, head, k):
        if head==None or head.next ==None or k==0:
            return head
        curr = head
        l = 1
        while curr.next:
            curr = curr.next
            l+=1
        r = k%l
        k = l-r
        curr.next = head
        while k>0:
            curr = curr.next
            k-=1
        head=curr.next
        curr.next = None
        return head
        