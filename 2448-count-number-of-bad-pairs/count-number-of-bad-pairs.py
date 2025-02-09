class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        ans = len(nums) * (len(nums) - 1) // 2
        for i, n in enumerate(nums):
            ans -= dict[n - i]
            dict[n - i] += 1
        return ans
            
