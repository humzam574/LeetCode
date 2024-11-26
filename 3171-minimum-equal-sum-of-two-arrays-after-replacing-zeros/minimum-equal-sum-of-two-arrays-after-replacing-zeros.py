class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        #return zero if num1 has no zeros and is less, or if num2 has no zeros and is less
        count1 = nums1.count(0)
        count2 = nums2.count(0)
        sum1 = sum(nums1) + count1
        sum2 = sum(nums2) + count2
        if (count1 == 0 and sum1 < sum2) or (count2 == 0 and sum2 < sum1):
            return -1
        return max(sum1, sum2)
        