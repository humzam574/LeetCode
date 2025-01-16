class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        heap = [[-balls, cnt] for balls, cnt in Counter(inventory).items()]
        heapify(heap)
        ans = 0
        while orders:
            balls, cnt = heappop(heap)
            balls *= -1
            nxt = -heap[0][0] if heap else 0
            groups = min(orders // cnt, balls - nxt)
            balls -= groups
            orders -= groups * cnt
            ans += (cnt*groups* (2 * balls + groups + 1) // 2) % 1000000007

            if not orders or balls != nxt:
                ans += (balls * orders) % 1000000007
                break
            heap[0][1] += cnt
        return ans % 1000000007
