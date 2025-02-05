class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for l in range(len(nums)):
            curr = nums[l]
            arr.append(curr)
            for r in range(l + 1, len(nums)):
                curr += nums[r]
                arr.append(curr)
        arr.sort()
        return sum(arr[left - 1:right]) % 1_000_000_007