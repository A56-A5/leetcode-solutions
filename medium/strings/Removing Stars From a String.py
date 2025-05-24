class Solution(object):
    def removeStars(self,s):
        r=[]
        for i in s:
            if i=="*":
                r.pop()
            else:
                r.append(i)
        return "".join(r)
            
        