class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # 0 ^ 0 = 0
        # 0 ^ 1 = 1 ^ 0 = 1
        # 1 ^ 1 = 0

        n = len(nums1)
        m = len(nums2)

        ans = 0
        if m % 2:
            for num in nums1:
                ans = ans ^ num
        if n % 2:
            for num in nums2:
                ans = ans ^ num
        return ans