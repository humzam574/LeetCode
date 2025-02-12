class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dict = {}
        ans = -1
        for num in nums:
            temp = 0
            temp2 = num
            while temp2:
                temp += temp2 % 10
                temp2 //= 10
            #print(temp)
            if temp in dict:
                val2 = dict[temp]
                ans = max(ans, num + val2)
                dict[temp] = max(num, val2)
            else:
                dict[temp] = num
        #print(dict)
        return ans