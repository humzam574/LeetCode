class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        dict = Counter(nums)
        ans = []
        for i in range(len(nums)):
            if dict[nums[i]] == 1 and nums[i] - 1 not in dict and nums[i] + 1 not in dict:
                ans.append(nums[i])
        return ans