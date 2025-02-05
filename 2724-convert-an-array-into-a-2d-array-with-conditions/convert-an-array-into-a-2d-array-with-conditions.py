class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dict = Counter(nums)
        ans = []
        while dict:
            temp = list(dict.keys())
            for item in temp:
                dict[item] -= 1
                if dict[item] == 0:
                    del dict[item]
            ans.append(temp)
        return ans