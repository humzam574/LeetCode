class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # def kadane(nums):
        #     res = -inf
        #     curr = 0
        #     for num in nums:
        #         curr = max(num, curr+num)
        #         res = max(res, curr)
        #     return res
        dict = {}
        for i in range(len(chars)):
            dict[chars[i]] = vals[i]
        nums = []
        for char in s:
            if char in dict:
                nums.append(dict[char])
            else:
                nums.append(ord(char) - ord('a') + 1)
        ans = -inf
        curr = 0
        for num in nums:
            curr = max(num, curr+num)
            ans = max(ans, curr)
        return max(0, ans)