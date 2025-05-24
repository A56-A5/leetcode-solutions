class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        x = nums[len(nums)/2]
        c = 0
        for i in nums:
            c += abs(x - i)

        return c
        