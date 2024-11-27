class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = sum(arr[0:k])
        thresh = k * threshold
        ans = int(window >= thresh)
        for i in range(k, len(arr)):
            window -= arr[i-k]
            window += arr[i]
            ans += int(window >= thresh)
        return ans