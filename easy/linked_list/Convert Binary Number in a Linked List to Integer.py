class Solution(object):
    def getDecimalValue(self, head):
        curr = head
        ans = 0
        while curr:
            ans = ans<<1
            ans = ans | curr.val
            curr = curr.next
        return ans 
        
