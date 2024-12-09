class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        d = [0]*len(nums)
        for i in range(1, len(nums)): d[i] = d[i-1] + int(nums[i] % 2 == nums[i-1] % 2)
        return [d[q[0]] == d[q[1]] for q in queries]