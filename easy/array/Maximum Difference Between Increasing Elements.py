class Solution(object):
    def maximumDifference(self, nums):
        i = nums[0]
        max_diff = -1
        
        for j in range(1, len(nums)):
            if nums[j] > i:
                max_diff = max(max_diff, nums[j] - i)
            else:
                i = nums[j]  
                
        return max_diff
