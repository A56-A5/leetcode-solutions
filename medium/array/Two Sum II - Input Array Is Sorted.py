class Solution(object):
    def twoSum(self, nums, target):
        i = len(nums)-1
        l = 0
        while i>l:
            if nums[i] + nums[l] == target:
                return [l+1,i+1]
            elif nums[i]+nums[l]>target:
                i-=1
            else:
                l+=1
        return [-1,-1]