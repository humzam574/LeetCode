class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,l = sorted(nums1 + nums2), len(nums1) + len(nums2)
        return a[l//2] if l % 2 else (a[l // 2] + a[l // 2 - 1])/2