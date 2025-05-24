class Solution(object):
    def firstMissingPositive(self, nums):
        nums = list(set(nums))
        nums = [i for i in nums if i>0]
        nums.sort()
        p=1
        for i in nums:
            if i==p:
                p+=1
                continue
            return p
        return p