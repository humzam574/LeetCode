class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans = 0
        l = 0
        for r, n in enumerate(nums):
            if n > right:
                delta = r - l
                if delta > 0:
                    ans += (delta * (delta + 1)//2)
                l = r + 1
        delta = r - l + 1
        if delta > 0:
            ans += (delta * (delta + 1)//2)
        right = left - 1
        l = 0
        for r, n in enumerate(nums):
            if n > right:
                delta = r - l
                if delta > 0:
                    ans -= (delta * (delta + 1)//2)
                l = r + 1
        delta = r - l + 1
        if delta > 0:
            ans -= (delta * (delta + 1)//2)
        return ans