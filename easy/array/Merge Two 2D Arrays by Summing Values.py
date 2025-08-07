class Solution(object):
    def mergeArrays(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)

        i = 0
        j = 0
        k = 0
        ans = list()
        while i < n and j < m:
            if nums1[i][0] == nums2[i][0]:
                ans[k][0] = nums1[i][0]
                ans[k][1] = nums1[i][1] + nums2[j][1]
                i+=1 
                j+=1 
                k+=1
            elif nums1[i][0] < nums2[i][0]:
                ans[k][0] = nums1[i][0]
                ans[k][1] = nums1[i][1]
                i+=1
                k+=1
            else:
                ans[k][0] = nums2[j][0]
                ans[k][1] = nums2[j][1]
                k+=1
                j+=1
        
        while i < n:
            ans[k][0] = nums1[i][0]
            ans[k][1] = nums1[i][1]
            i+=1
            k+=1
        while j < n:
            ans[k][0] = nums2[j][0]
            ans[k][1] = nums2[j][1]
            k+=1
            j+=1
        return ans 
