class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        heap = [(-v, k) for k, v in Counter(barcodes).items()]
        heapify(heap)
        ans = []
        prev = None
        while heap:
            a, b = heappop(heap)
            if b == prev:
                c, d = heappop(heap)
                ans.append(d)
                heappush(heap, (a,b))
                prev = d
                if c < -1:
                    heappush(heap, (c+1, d))
                    
            else:
                ans.append(b)
                prev = b
                if a < -1:
                    heappush(heap, (a+1, b))
                    
        return ans