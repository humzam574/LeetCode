class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        dict, v = defaultdict(int), 0
        for i in range(1, len(nums)): v, dict[i] = v + int(nums[i]%2 == nums[i-1]%2), v + int(nums[i]%2 == nums[i-1]%2)
        return [dict[query[0]] == dict[query[1]] for query in queries]