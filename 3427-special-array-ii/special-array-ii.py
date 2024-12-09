class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        dict, v = defaultdict(int), 0
        for i in range(1, len(nums)):
            if nums[i]%2 == nums[i-1]%2: v+=1
            dict[i] = v
        return [dict[query[0]] == dict[query[1]] for query in queries]