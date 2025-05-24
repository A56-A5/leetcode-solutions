class Solution(object):
    def hasAllCodes(self, s, k):
        if k > len(s): 
            return False
        
        ss = set()

        for i in range(len(s)-k+1):
            ss.add(s[i:i+k])

        x  = True if (len(ss) == 2**k) else False
        return x    
