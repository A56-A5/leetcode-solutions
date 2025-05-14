class Solution(object):
    def canAliceWin(self, nums):
        single = 0
        double = 0
        for i in nums:
            if i>9:
                double+=i
            else:
                single+=i
        return not (single==double)
