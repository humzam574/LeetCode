class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        dict = defaultdict(int)
        dict[0] = 1
        curr = 0
        for num in nums:
            curr += num
            ans += dict[curr - k]
            dict[curr] += 1
        return ans