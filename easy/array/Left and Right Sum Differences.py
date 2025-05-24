class Solution(object):
    def leftRightDifference(self, nums):
        leftSum = list()
        rightSum = list()
        ans = list()

        leftSum.append(0)
        for i in range(1,len(nums)):
            s=0
            for j in range(i):
                s += nums[j]
            leftSum.append(s)

        for i in range(len(nums)-1):
            s=0
            for j in range(i+1,len(nums)):
                s += nums[j]
            rightSum.append(s)
        rightSum.append(0)

        for i in range(len(nums)):
            if rightSum[i] >= leftSum[i]:
                x = rightSum[i] - leftSum[i]
            else: 
                x = leftSum[i] - rightSum[i]
            ans.append(x)

        return ans

        
