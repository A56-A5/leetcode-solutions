class Solution(object):
    def vowelStrings(self, words, left, right):
        ans = 0
        for i in range(left,right+1):
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                ans += 1
        return ans 
        
