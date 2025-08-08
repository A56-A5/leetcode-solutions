class Solution(object):
    def guessNumber(self, n):
        top = n
        low = 1
        while low <= top:
            mid = low+(top-low)/2
            if guess(mid) < 0:
                top = mid-1
            elif guess(mid) > 0:
                low = mid+1
            else:
                return mid 
            
