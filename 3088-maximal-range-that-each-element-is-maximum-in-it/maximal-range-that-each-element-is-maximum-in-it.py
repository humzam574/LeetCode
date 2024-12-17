class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        stack = []
        for i, n in enumerate(nums):
            while stack and n > stack[-1][0]:
                sn, si = stack.pop()
                ans[si] = i - si
            stack.append((n, i))
        for i,n in stack:
            ans[n] = len(ans) - n
        stack = []
        a2 = [0] * len(nums)
        nums = nums[::-1]
        for i, n in enumerate(nums):
            while stack and n > stack[-1][0]:
                sn, si = stack.pop()
                if i - si > 1:
                    a2[si] = i - si - 1
            stack.append((n,i))
        for i,n in stack:
            a2[n] += (len(ans) - n - 1)
        a2 = a2[::-1]
        res = []
        for i in range(len(a2)):
            res.append(ans[i]+a2[i])
        return res