class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        #handle edge cases and find the longest gap
        #if odd number of zeros, return num // 2
        #if even number of zeros, return num // 2
        first = -1
        last = -1
        prev = -1
        high = -1
        for i in range(len(seats)):
            if seats[i]:
                last = i
                if first == -1:
                    first = i
                high = max(high, i - prev)
                prev = i
        #high = max(high, i - prev)
        #print(high)
        return max(high // 2, i - last, first)
