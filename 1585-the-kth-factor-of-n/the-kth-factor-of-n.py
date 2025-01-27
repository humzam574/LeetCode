class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt = 0
        other = []
        for i in range(1, 1 + int(n ** 0.5)):
            if n % i == 0:
                cnt += 1
                if cnt == k: return i
                if n // i != i:
                    other.append(n // i)
        if k - cnt > len(other): return -1
        for i in range(len(other) - 1, -1, -1):
            cnt += 1
            if cnt == k:
                return other[i]