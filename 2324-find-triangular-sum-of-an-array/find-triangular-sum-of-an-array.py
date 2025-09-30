class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums
        for i in range(n-1, 0, -1):
            # print(i)
            # print(prev)
            # print()
            arr = [0] * i
            for j in range(i):
                arr[j] = (prev[j] + prev[j+1]) % 10
            # print(arr)
            # print()
            prev = arr
        return sum(prev)