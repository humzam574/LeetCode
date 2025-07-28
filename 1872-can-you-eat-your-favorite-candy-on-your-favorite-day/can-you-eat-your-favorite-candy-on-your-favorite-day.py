class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        presum = list(accumulate(candiesCount, initial=0))
        ans = []
        for i, end, cost in queries:
            if (presum[i] < (end + 1) * cost and presum[i + 1] > end):
                ans.append(True)
            else:
                ans.append(False)
        return ans