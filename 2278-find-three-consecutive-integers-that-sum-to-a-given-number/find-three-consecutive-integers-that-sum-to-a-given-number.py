class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3: return []
        k = (num-3) // 3
        return [k ,k + 1,k + 2]