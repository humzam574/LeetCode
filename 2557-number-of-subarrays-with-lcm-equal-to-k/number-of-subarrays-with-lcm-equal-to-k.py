class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            curr = nums[i]
            for j in range(i, n):
                curr = lcm(curr, nums[j])
                if curr == k:
                    ans += 1
                elif curr > k:
                    break
        return ans