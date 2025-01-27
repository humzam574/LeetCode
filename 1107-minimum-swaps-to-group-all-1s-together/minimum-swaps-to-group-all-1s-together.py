class Solution:
    def minSwaps(self, data: List[int]) -> int:
        offset = data.count(1)
        curr = data[:offset].count(1)
        ans = offset - curr
        for r in range(offset, len(data)):
            curr += data[r] - data[r-offset]
            ans = min(ans, offset - curr)
        return ans

