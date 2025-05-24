class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        s.reverse()
        return " ".join(s)