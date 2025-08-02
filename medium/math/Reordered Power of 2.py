class Solution(object):
    def reorderedPowerOf2(self, n):
        digits = sorted(str(n))
        for i in range(31): 
            power_digits = sorted(str(1 << i))
            if digits == power_digits:
                return True
        return False
