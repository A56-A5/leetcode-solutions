class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        if len(nums) < 2:
            return 0
        m = 0
        k=0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                k = nums[i] - nums[i-1]
            else: 
                k = nums[i-1] - nums[i]
            if k>m:
                m=k
        return m