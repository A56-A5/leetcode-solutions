class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 = sorted(nums1 + nums2)
        l = len(nums1)
        if len(nums1)%2==0:
            return (nums1[l//2-1]+nums1[l//2])/2.000
        else:
            return nums1[l//2]
