class Solution:
    
    def rob(self, nums: List[int]) -> int:
        def rob1(ns):
            memo = defaultdict(int)
            def dp(i, tot):
                if i >= len(ns) or i in memo: return tot+memo[i]
                memo[i] = max(dp(i + 2, ns[i]), dp(i + 1, 0))
                return tot+memo[i]
            return dp(0, 0)
        pos1 = rob1(nums[1:])
        if len(nums) == 1:
            return nums[0]
        nums.pop()
        pos2 = rob1(nums)
        return max(pos1, pos2)