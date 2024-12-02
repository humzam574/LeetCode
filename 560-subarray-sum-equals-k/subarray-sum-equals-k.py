class Solution:
    def subarraySum(self, nums: List[int], goal: int) -> int:
        dict, curr, ans = defaultdict(int), 0, 1
        for i in range(len(nums)):
            curr+=nums[i]
            ans, dict[curr] = ans + (curr == goal) + dict[curr - goal], dict[curr] + 1
        return ans-1