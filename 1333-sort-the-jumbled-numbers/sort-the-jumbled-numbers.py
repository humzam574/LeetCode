class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def conv(num):
            ans = ""
            for char in str(num):
                ans+=str(mapping[int(char)])
            return int(ans)
        ans = []
        for num in nums:
            ans.append((num, conv(num)))
        ans.sort(key = lambda x : x[1])
        return [a[0] for a in ans]