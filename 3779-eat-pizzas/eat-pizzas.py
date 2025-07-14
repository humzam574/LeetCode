class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        #select the odds first, then get all the evens
        #given there are x days
        #if x is even, you have x/2 odds
        #if x is odd, you have x+1/2 odds

        n = len(pizzas)
        x = n // 4
        odds = (x + 1) // 2
        ans = 0
        ans += sum(pizzas[n-odds:])
        ptr = n - odds - 2
        #[0, ..., 0, 1, 2, 3, 4, 5, 6, 7]
        for i in range((x//2)):
            ans+=pizzas[ptr]
            ptr-=2
        return ans