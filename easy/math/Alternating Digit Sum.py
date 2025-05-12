class Solution(object):
    def alternateDigitSum(self, n):
        ans = 0 
        c = 1
        for i in str(n):
            ans += int(i)*c
            c*=-1
        return ans
        
