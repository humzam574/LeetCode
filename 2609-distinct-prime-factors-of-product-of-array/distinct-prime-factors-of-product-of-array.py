class Solution:
    def distinctPrimeFactors(self, n: List[int]) -> int:
        ans = 0
        curr = 2
        nums = 1
        for g in n:
            nums*=g
        while nums != 1:
            if nums % curr == 0:
                ans += 1
                while nums % curr == 0:
                    nums = nums // curr
            curr += 1
        return ans