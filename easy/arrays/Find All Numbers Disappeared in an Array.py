class Solution(object):
    def findDisappearedNumbers(self, nums):
        l = set([i for i in range(1,len(nums)+1)])
        return list(l - set(nums))
