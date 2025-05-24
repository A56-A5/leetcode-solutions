class Solution(object):
    def findMatrix(self, nums):
        ans = list()
        s = set()
        while nums:
            row = list()
            i=0
            while i<len(nums):
                if nums[i] not in s:
                    s.add(nums[i])
                    row.append(nums[i])
                    nums.pop(i)
                    i-=1
                i+=1
            ans.append(row)
            s.clear()
        return ans



