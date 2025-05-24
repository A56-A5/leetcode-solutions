class Solution(object):
    def sortList(self, head):
        node = head
        r = list()
        while node:
            r.append(node.val)
            node = node.next
        r.sort()

        node = head
        for i in range(len(r)):
            node.val = r[i]
            node = node.next
        return head
        