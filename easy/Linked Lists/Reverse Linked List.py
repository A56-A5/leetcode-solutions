class Solution(object):
    def reverseList(self, head):
        l = list()
        x = head
        if not x or not head.next:
            return head

        while x:
            l.append(x.val)
            x = x.next
        x = head
        while x:
            x.val = l.pop()
            x = x.next
        return head
