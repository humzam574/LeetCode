class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        dict = Counter(nums[:k])
        ans[0] = len(dict.keys())
        l, r = 0, k
        #print(dict.keys())
        for r in range(k, len(nums)):
            dict[nums[l]] -= 1
            if dict[nums[l]] == 0:
                del dict[nums[l]]
            dict[nums[r]] += 1
            l += 1
            ans[l] =len(dict.keys())
            #print(dict.keys())
        return ans