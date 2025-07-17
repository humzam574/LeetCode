class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            nums[i] %= k
        print(nums)
        ans = 2
        dp = [[0] * (k) for i in range(k)]
        for v in nums:
            for prev in range(k):
                if prev == v:
                    continue
                if dp[prev][v] > 0:
                    new_len = dp[prev][v] + 1
                    if new_len > dp[v][prev]:
                        dp[v][prev] = new_len
                    if new_len > ans:
                        ans = new_len
        
            for other in range(k):
                if other == v:
                    continue
                if dp[v][other] < 1:
                    dp[v][other] = 1
        
        return max(ans, max(Counter(nums).values()))