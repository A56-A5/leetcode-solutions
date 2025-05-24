class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        if not head or not head.next:
            return head
        def gcd(a,b):
            while b:
                a,b = b,a%b
            return a

        prev = head
        while prev.next:
            curr = prev.next
            x = gcd(prev.val,curr.val)
            g = ListNode(x)
            prev.next = g
            g.next = curr
            prev = curr
        return head
            
        