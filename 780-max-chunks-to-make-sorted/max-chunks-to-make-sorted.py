class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        prfx, exp, curr = 0, 0, 0
        for i, num in enumerate(arr): prfx, exp, curr = prfx + num, exp + i, curr + (prfx + num == exp + i)
        return curr