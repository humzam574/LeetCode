class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        #create a set with all the combos
        #or a dictionary with key product value pair
        dict = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                dict[nums[i]*nums[j]]+=1
        #print(dict) #n * (n - 1) * 4
        ans = 0
        for count in dict.values():
            if count > 1:
                ans += (count * (count - 1)) * 4
        return ans