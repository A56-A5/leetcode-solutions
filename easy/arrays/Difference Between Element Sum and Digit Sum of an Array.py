class Solution(object):
    def differenceOfSum(self, nums):
        ele_sum = 0
        dig_sum = 0 
        for i in nums:
            ele_sum += i 
            while i > 0:
                dig_sum += i % 10 
                i/=10 
        return abs(dig_sum - ele_sum)
        