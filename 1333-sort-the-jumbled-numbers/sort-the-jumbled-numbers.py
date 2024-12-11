class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        ans = []
        for num in nums: ans.append((num, int("".join(str(mapping[int(char)]) for char in str(num)))))
        return [a[0] for a in sorted(ans, key = lambda x : x[1])]