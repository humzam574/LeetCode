class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        count1, count2 = nums1.count(0), nums2.count(0)
        sum1 = sum(nums1) + count1
        sum2 = sum(nums2) + count2
        return -1 if (count1 == 0 and sum1 < sum2) or (count2 == 0 and sum2 < sum1) else max(sum1, sum2)
        