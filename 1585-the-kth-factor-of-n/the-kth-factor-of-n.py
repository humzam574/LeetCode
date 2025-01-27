class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt, other = 0, []
        for i in range(1, 1 + int(n ** 0.5)):
            if n % i == 0:
                cnt += 1
                if cnt == k: return i
                if n // i != i: other.append(n // i)
        return -1 if k - cnt > len(other) else other[-k + cnt]