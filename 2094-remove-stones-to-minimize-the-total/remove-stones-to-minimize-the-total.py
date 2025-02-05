import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxv = max(piles)
        bucket = [0] * (maxv + 1)

        for p in piles:
            bucket[p] += 1
        
        for i in range(maxv, -1, -1):
            if not k:
                break
            
            cur = min(k, bucket[i])
            bucket[i] -= cur
            bucket[(i + 1) // 2] += cur

            k -= cur
        
        sumv = 0
        for i in range(len(bucket)):
            sumv += bucket[i] * i
        
        return sumv