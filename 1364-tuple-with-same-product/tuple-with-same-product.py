class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dict, n, ans = defaultdict(int), len(nums), 0
        for i in range(n):
            for j in range(i + 1, n): dict[nums[i]*nums[j]] += 1
        for count in dict.values():
            if count > 1: ans += (count * (count - 1)) * 4
        return ans