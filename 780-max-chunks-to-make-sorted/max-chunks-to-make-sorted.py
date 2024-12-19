class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        #backtracking
        #take every split and see if you can sort and recombine
        #if so throw it into a max variable

        prfx, exp, curr = 0, 0, 0
        for i, num in enumerate(arr):
            prfx += num
            exp += i
            if prfx == exp:
                curr += 1
        return curr