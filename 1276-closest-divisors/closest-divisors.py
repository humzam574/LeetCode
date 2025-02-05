class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        upper = int((num+2) ** 0.5)
        for i in range(upper, 0, -1):
            if (num+1) % i == 0: return [(num+1)//i, i]
            if (num+2) % i == 0: return [(num+2)//i, i]