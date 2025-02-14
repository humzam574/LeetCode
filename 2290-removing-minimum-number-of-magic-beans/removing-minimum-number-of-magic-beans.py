class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        ans = float('inf')
        total = sum(beans)
        length = len(beans)
        for bean in beans:
            curr = total - length * bean
            length -= 1
            if curr < ans: ans = curr
        return ans