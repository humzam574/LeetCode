class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        #create a set with all the combos
        #or a dictionary with key product value pair
        dict = defaultdict(list)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                dict[nums[i]*nums[j]].append({nums[i], nums[j]})
        #print(dict) #n * (n - 1) * 4
        ans = 0
        for arr in dict.values():
            ans += (len(arr) * (len(arr) - 1)) * 4
        return ans