class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = [0] * len(queries)
        n = len(nums)
        low, high = nums[0], nums[-1]
        prefix = list(nums)
        for i in range(1, len(nums)):
            prefix[i] += prefix[i - 1]
        for i,q in enumerate(queries):
            if q <= low or q >= high:
                ans[i] = abs(prefix[-1] - q*n)
            else:
                idx = bisect_left(nums, q)
                ans[i] = idx*q - prefix[idx - 1] + prefix[-1] - prefix[idx - 1] - (n - idx)*q
        return ans