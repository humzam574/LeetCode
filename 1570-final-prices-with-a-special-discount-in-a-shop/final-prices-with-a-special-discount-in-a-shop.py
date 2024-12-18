class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        nextsmaller = prices[:]

        for i,p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                idx = stack.pop()
                nextsmaller[idx] = prices[idx] - p
            stack.append(i)
        

        return nextsmaller