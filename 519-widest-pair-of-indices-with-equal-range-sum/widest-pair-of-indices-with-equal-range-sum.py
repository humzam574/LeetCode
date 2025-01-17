class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) == 1: return int(nums1[0] == nums2[0])
        ans, dict, sum1, sum2 = 0, {}, nums1[0], nums2[0]
        nums = [sum1 - sum2] + [0] * (len(nums1)-1)
        for i in range(1, len(nums1)): sum1 += nums1[i]; sum2 += nums2[i]; nums[i] = sum1 - sum2
        for i, n in enumerate(nums):
            if n == 0: ans = max(ans, i + 1)
            elif n in dict: ans = max(ans, i - dict[n])
            else: dict[n] = i
        return ans