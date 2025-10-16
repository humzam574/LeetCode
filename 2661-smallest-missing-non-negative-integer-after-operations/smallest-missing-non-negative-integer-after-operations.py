class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        arr = [0] * value
        for num in nums:
            arr[num % value]+=1
        # print(arr)
        low = inf
        idx = -1
        for i,x in enumerate(arr):
            if x < low:
                low = x
                idx = i
        
        return value*low + idx
