class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        #j - i != nums[j] - nums[i]
        #+1 from before
        #NOT nums[i] - i == nums[j] - j
        dict = defaultdict(int)
        ans = 0
        for i, n in enumerate(nums):
            ans += (i - dict[n - i])
            dict[n - i] += 1
        return ans
            
