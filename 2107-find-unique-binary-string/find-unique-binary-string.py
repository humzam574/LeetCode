class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)
        def dfs(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr
                else:
                    return ""
            return dfs(curr + "1") or dfs(curr + "0")
        return dfs("")