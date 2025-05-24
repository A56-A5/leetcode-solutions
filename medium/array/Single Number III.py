class Solution(object):
    def singleNumber(self, nums):
        c = {}
        for n in nums:
            if n in c:
                c[n] += 1
            else:
                c[n] = 1
        r = list()

        for i,n in c.items():
            if n == 1:
                r.append(i)
        return r