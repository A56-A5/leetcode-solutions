class Solution(object):
    def divide(self, a, b):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if a == INT_MIN and b == -1:
            return INT_MAX
            
        negative = (a < 0) != (b < 0)
        
        a, b = abs(a), abs(b)
        result = 0
        
        while a >= b:
            temp, multiple = b, 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            result += multiple
        
        return -result if negative else result
