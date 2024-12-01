class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        costs, ans, curr = [i + 1 for i in range(26)], 0, 0
        for c, v in zip(chars, vals): costs[ord(c) - 97] = v    
        for char in s:
            curr += costs[ord(char) - 97]
            if curr < 0: curr = 0
            if curr > ans: ans = curr
        return ans