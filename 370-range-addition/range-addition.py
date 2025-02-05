class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * (length + 1)
        for l, r, a in updates: arr[l] += a; arr[r + 1] -= a
        for i in range(1, len(arr) - 1): arr[i] = arr[i - 1] + arr[i]
        return arr[:-1]