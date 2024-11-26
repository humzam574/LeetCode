class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        high = max(nums)
        low = min(nums)
        depth = defaultdict(int)
        for num in nums:
            depth[num]=1
            top = 0
            for i in range(num - 1, low-1, -1):
                top = max(top, depth[i])
            depth[num]+=top
        #print(depth)
        return max(depth.values())