class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        arr = sorted(nums1 + nums2)
        if length % 2 == 0:
            mid = length // 2
            return (arr[mid] + arr[mid - 1])/2
        return arr[length//2]