class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        dict = {}
        if len(nums1) == 1: return int(nums1[0] == nums2[0])
        nums, ans = [0] * len(nums1), 0
        nums[0] = nums1[0] - nums2[0]
        for i in range(1, len(nums1)):
            nums1[i] += nums1[i - 1]
            nums2[i] += nums2[i - 1]
            nums[i] = nums1[i] - nums2[i]
        for i, n in enumerate(nums):
            if n == 0: ans = max(ans, i + 1)
            elif n in dict: ans = max(ans, i - dict[n])
            else: dict[n] = i
        return ans

            