class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        #two pointer and a dictionary
        dict = defaultdict(int)
        ans = 0
        l, r = 0, 0
        while r < len(nums):
            # print("l = " + str(l) + " r = " + str(r))
            # print(dict)
            dict[nums[r]]+=1
            if dict[nums[r]] > k:
                while dict[nums[r]] > k:
                    dict[nums[l]]-=1
                    l+=1
            r+=1
            ans = max(ans, r - l)
        return ans