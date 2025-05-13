class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        temp = sorted(arr)
        n = len(arr)
        mid = temp[(n - 1) // 2]
        arr.sort(key = lambda x : (abs(x - mid), x))
        #print(mid)
        #print(arr)
        return arr[n-k:]