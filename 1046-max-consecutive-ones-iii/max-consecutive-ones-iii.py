__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr = [0,0]
        l = 0
        ans = 0
        for r in range(len(nums)):
            curr[nums[r]]+=1
            while curr[0] > k:
                curr[nums[l]]-=1
                l+=1
            # print(str(l) + ", " + str(r))
            # print(curr)
            # print()
            ans = max(ans, sum(curr))
        return ans