class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        #size n which is multiple of 3
        #get the minimum value min
        #get the max value max

        #grab the n/3 numbers within min+k
        #grab the n/3 numbers within max-k
        ans = []
        n = len(nums)
        curr = 0
        nums.sort()
        for i in range(n//3):
            arr = nums[curr:curr+3]
            if arr[-1] - arr[0] > k:
                return []
            ans.append(arr)
            curr += 3
        return ans


            