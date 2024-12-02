class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        arr = [] 
        zeros = 0
        for c in nums:
            if c == 0:
                zeros += 1
            else:
                arr.append(zeros)
                zeros = 0
        
        ones = len(arr)
        if ones < goal:
            return 0
        arr.append(zeros)
        out = 0
        
        if goal == 0:
            for x in arr:
                out += (x * (x+1)) // 2
            return out

        for i in range(ones-goal+1):
            out += (arr[i]+1)*(arr[i+goal]+1)
        return out
