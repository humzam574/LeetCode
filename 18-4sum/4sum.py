class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #O(n^3) + two sum
        #pick every group of 3 numbers
        #two sum the rest
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                prev = set()
                for l in range(j+1):
                    if l != i and l != j:
                        prev.add(nums[l])
                tot = nums[i] + nums[j]
                for k in range(j+1, n):
                    #stuff
                    if target - tot - nums[k] in prev:
                        ans.add(tuple(sorted([nums[i], nums[j], nums[k], target - tot - nums[k]])))
                    prev.add(nums[k])
        print(ans)
        ans2 = []
        for val in ans:
            ans2.append(list(val))
        return ans2
                    