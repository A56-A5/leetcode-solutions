class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] > nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        return nums
        