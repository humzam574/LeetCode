class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        ans = []
        delta = 0
        num += 1
        for i in range(1, 1+int(math.sqrt(num))):
            if num % i == 0:
                ans = sorted([i, num // i])
                delta = abs(i - num // i)
        num += 1
        for i in range(1, 1+int(math.sqrt(num))):
            if num % i == 0:
                if abs(i - num // i) < delta:
                    ans = sorted([i, num//i])
        return ans