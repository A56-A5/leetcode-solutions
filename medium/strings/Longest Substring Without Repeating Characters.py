class Solution(object):
    def lengthOfLongestSubstring(self, s):
        a,st=0,""
        if len(s)==1:
            return 1
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[j] in st:
                    if len(st)>a:
                        a= len(st)
                    st=""
                    break
                st+=s[j]
        return a
        
