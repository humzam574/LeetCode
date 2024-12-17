class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        l = len(nums)
        a1, a2 = [0] * l, [0] * l
        s1, s2 = [], []
        for i in range(l):
            n = nums[i]
            while s1 and n > s1[-1][0]:
                sn, si = s1.pop()
                a1[si] = i - si
            s1.append((n, i))
            n = nums[l - i - 1]
            while s2 and n > s2[-1][0]:
                sn, si = s2.pop()
                a2[si] = i - si - 1
            s2.append((n,i))
        for i,n in s1:
            a1[n] += l - n
        l -= 1
        for i,n in s2:
            a2[n] += (l - n)
        return [a1[i]+a2[l-i] for i in range(l+1)]