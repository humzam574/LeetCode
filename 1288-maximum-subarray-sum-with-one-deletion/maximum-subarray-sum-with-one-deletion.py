class Solution:
    def maximumSum(self, arr: List[int]):
        mx = n0 = n1 = -inf
        for i, num in enumerate(arr): n1 = max(n0,  n1 + num); n0 = max(num, n0 + num); mx = max(mx,  n1,   n0)
        return mx