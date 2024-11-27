class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window, ans = sum(arr[0:k]) - (k*threshold), 0
        for i in range(k, len(arr)): ans, window = ans + int(window >= 0), window + arr[i] - arr[i-k]
        return ans + int(window >= 0)