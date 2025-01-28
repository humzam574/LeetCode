class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = -1
        #k is the deltas of all the numbers previous
        #[1, 2, 2, 3, 6, 8] k = 4
        #[0, 1, 0, 1, 3, 1]
        n2 = [0] * n
        for i in range(1, n):
            n2[i] = nums[i] - nums[i - 1]
        #print(n2)
        l = 0
        curr = 0
        for r in range(n):
            curr += n2[r]*(r - l)
            while curr > k and l <= r:
                curr = curr - nums[r] + nums[l]
                l += 1
            ans = max(ans, r - l + 1)
            #print("l: " + str(l) + " r: " + str(r) + " curr: " + str(curr))
        return ans