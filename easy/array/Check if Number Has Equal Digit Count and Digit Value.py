class Solution(object):
    def digitCount(self, num):
        nums = [int(i) for i in str(num)]

        for i in range(len(nums)):
            if nums.count(i) != nums[i]:
                return False
        return True
        
