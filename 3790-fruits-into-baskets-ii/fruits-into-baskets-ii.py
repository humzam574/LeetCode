class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        rem = [True] * n
        ans = n
        i = 0
        for val in fruits:
            for i in range(n):
                if baskets[i] >= val and rem[i]:
                    rem[i] = False
                    ans-=1
                    break
            
            
        return ans