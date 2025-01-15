class Solution:
    def jump(self, nums: List[int]) -> int:
        answer, n, end, far = 0, len(nums), 0, 0
        for i in range(n - 1):
            far = max(far, i + nums[i])
            if i == end: answer, end = answer + 1, far
        return answer