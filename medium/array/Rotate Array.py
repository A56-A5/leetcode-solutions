class Solution(object):
    def rotate(self, nums, k):
        k%=len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        