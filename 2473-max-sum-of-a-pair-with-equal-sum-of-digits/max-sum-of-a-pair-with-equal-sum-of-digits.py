class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dict = {}
        ans = -1
        for num in nums:
            temp = sum(int(char) for char in str(num))
            #print(temp)
            if temp in dict:
                val2 = dict[temp]
                ans = max(ans, num + val2)
                dict[temp] = max(num, val2)
            else:
                dict[temp] = num
        #print(dict)
        return ans