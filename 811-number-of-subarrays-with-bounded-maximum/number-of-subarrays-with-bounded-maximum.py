class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def search(high):
            ans = 0
            l = 0
            for r, n in enumerate(nums):
                if n > high:
                    delta = r - l
                    if delta > 0:
                        ans += (delta * (delta + 1)//2)
                    l = r + 1
            delta = r - l + 1
            if delta > 0:
                ans += (delta * (delta + 1)//2)
            return ans
        return search(right) - search(left - 1)