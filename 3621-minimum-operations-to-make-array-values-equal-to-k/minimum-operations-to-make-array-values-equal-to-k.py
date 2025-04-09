class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        arr = list(set(nums))
        arr.sort()
        print(arr)
        ans = len(arr)
        for i in range(len(arr)):
            if arr[i] < k:
                return -1
            if arr[i] > k:
                return ans
            ans -= 1
        return ans