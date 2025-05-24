class Solution(object):
    def canSeePersonsCount(self, heights):
        ans = [0 for i in range(len(heights))]
        l = list()
        for i,j in enumerate(heights):
            while l and heights[l[-1]] <=j:
                ans[l.pop()] +=1
            if l:
                ans[l[-1]] +=1
            l.append(i)
        return ans
        