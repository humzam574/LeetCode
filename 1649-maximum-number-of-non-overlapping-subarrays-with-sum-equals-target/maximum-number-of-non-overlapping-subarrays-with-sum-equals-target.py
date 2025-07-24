class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        #nvm dis a prefix sum
        n = len(nums)
        prefix = [0] * (n)
        #basically a buffed two sum
        prev = {0}#set()

        for i in range(n):
            prefix[i] = prefix[i - 1] + nums[i]
        print(prefix)
        #prefix is all the numbers before and including i
        ans = 0
        for i in range(n):
            if prefix[i] - target in prev:
                ans += 1
                prev = set()
            prev.add(prefix[i])
        
        return ans