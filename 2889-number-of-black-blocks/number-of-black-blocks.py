class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        count, blocks = [(m-1)*(n-1),0,0,0,0], {}
        for x, y in coordinates:
            for i in range(max(0, x - 1), min(m - 1, x + 1)):
                for j in range(max(0, y - 1), min(n - 1, y + 1)):
                    if (i, j) not in blocks:
                        blocks[(i, j)] = 0
                    count[blocks[(i, j)]] -= 1
                    blocks[(i, j)] += 1
                    count[blocks[(i, j)]] += 1
        return  count#(m - 1) * (n - 1) - sum(count[1:])