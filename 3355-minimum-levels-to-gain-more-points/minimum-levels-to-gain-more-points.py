class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        arr = [-1 if i == 0 else i for i in possible]
        sm = sum(arr)
        curr = arr[0]
        for i in range(1, len(arr)):
            if 2*curr > sm:
                return i
            curr+=arr[i]
        return -1