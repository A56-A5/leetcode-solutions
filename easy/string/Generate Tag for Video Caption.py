class Solution(object):
    def generateTag(self, caption):
        w = caption.split()
        ans = "#"
        for i, w in enumerate((w)):
            if i == 0:
                ans += w.lower()
            else:
                if w:
                    ans += w.capitalize()
        ans = ans[:100]    
        
        return ans
