class Solution(object):
    def countPartitions(self, nums):
        ans = 0
        for i in range(len(nums)-1):
            x = abs(sum(nums[0:i+1]) - sum(nums[i+1:]))
            if x%2 == 0:
                ans+=1
        return ans
