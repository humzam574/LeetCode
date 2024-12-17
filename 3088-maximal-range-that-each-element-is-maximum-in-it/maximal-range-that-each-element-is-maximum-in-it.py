class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        l = len(nums)
        a1 = [0] * l
        stack = []
        for i, n in enumerate(nums):
            while stack and n > stack[-1][0]:
                sn, si = stack.pop()
                a1[si] = i - si
            stack.append((n, i))
        for i,n in stack:
            a1[n] = l - n
        stack = []
        a2 = [0] * l
        l -= 1
        for i in range(l, -1, -1):
            n, i = nums[i], l - i
            while stack and n > stack[-1][0]:
                sn, si = stack.pop()
                a2[si] = max(0, i - si - 1)
            stack.append((n,i))
        for i,n in stack:
            a2[n] += (l - n)
        ans = []
        for i in range(l + 1):
            ans.append(a1[i]+a2[l-i])
        return ans