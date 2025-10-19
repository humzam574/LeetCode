class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        maxSum, runSum = 0, 0
        seen = set()
        for r in range (len (nums)):
            # NOT DISTINCT / LENGTH CASE
            runSum += nums[r]
            while nums[r] in seen or r-l+1>k:
                seen.remove(nums[l])
                runSum-=nums[l]
                l += 1
                
            # print(str(l) + ", " + str(r) + " " + str(runSum))
            if r-l+ 1 == k:
                maxSum= max (maxSum, runSum)
            seen.add(nums[r])
            
        return maxSum