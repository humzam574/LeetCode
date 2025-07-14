class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        res = 0
        day = len(pizzas) // 4 
        odd_day = day // 2 + day % 2
        even_day = day - odd_day 
        res += sum(pizzas[-odd_day:])
        res += sum(pizzas[-odd_day - even_day * 2 : -odd_day : 2])
        return res