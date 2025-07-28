class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        #do some sort of preprocessing to be able to calculate in O(1) for each query
        #prefix sum candiescount
        #do a lower bound where you eat one candy per day, see what candy you're on
        #do an upper bound of eating max candies per day
        #see if your favorite type is within those bounds
        n = len(candiesCount)
        #make a prefix sum and binary search it
        for i in range(1, n):
            candiesCount[i]+=candiesCount[i-1]
        # print(candiesCount)
        candiesCount.append(0)
        ans = []
        for target, day, cap in queries:
            lower = (day+1)
            upper = (day+1)*cap
            #binary search lower and upper
            if lower <= candiesCount[target] and candiesCount[target-1] < upper:
                ans.append(True)
            else:
                ans.append(False)
        return ans