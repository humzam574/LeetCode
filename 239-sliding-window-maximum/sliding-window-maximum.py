class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        if k >= len(nums): return [max(nums)]
        dq = deque()
        for i in range(k):
            num = nums[i]
            while dq and dq[-1] < num: dq.pop()
            dq.append(num)
        ans = [dq[0]]
        for i in range(k, len(nums)):
            l, r = nums[i - k], nums[i]
            if l == dq[0]: dq.popleft()
            while dq and dq[-1] < r: dq.pop()
            dq.append(r)
            ans.append(dq[0])
        return ans