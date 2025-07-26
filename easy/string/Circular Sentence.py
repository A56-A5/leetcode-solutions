class Solution(object):
    def isCircularSentence(self, s):
        for i in range(len(s)):
            if s[i] == ' ':
                if s[i-1] != s[i+1]:
                    return False
        return s[0] == s[len(s)-1]
