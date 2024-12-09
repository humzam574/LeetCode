class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        d, v = [0]*len(nums), 0
        for i in range(1, len(nums)):
            #if nums[i] % 2 == nums[i-1] % 2: v+=1
            v += int(nums[i] % 2 == nums[i-1] % 2)
            d[i] = v
        return [d[q[0]] == d[q[1]] for q in queries]