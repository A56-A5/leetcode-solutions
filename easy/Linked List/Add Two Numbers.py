class Solution:
    def addTwoNumbers(self, l1, l2):
        ans = res = ListNode(0)
        n1 = n2 = ""
        while l1 or l2:
            if l1:
                n1 = str(l1.val) + n1
                l1 = l1.next
            if l2:
                n2 = str(l2.val) + n2
                l2 = l2.next
        r = int(n1)+int(n2)
        if r==0:
            return res
        while r!=0:
            x = r%10
            r /= 10
            ans.next = ListNode(x)
            ans = ans.next
        return res.next

        
        
