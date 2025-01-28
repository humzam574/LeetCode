class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        max_pre = [-1]*n
        max_post = [-1]*n
        for i in range(n-1):
            for j in range(i + 1, n):
                if prices[j] > prices[i]:
                    max_pre[j] = max(max_pre[j], profits[i])
                    max_post[i] = max(max_post[i], profits[j])
        res = -1
        for i, p in enumerate(profits):
            if max_pre[i] != -1 and max_post[i] != -1:
                res = max(res, p + max_pre[i] + max_post[i])
        
        return res

    # or faster use sortedSet
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        def find(left, prices, profits):
            ss = SortedSet()
            for index in range(len(prices)):
                idx = ss.bisect_left((prices[index], float('-Inf')))
                if idx > 0:
                    left[index] = ss[idx - 1][1]    # ss would be strickly increasing of "price, profit"
                
                # update sortedset
                #    1. no need to insert current value
                if idx > 0 and ss[idx - 1][1] >= profits[index]:
                    continue             
                #    2. remove elements in ss if no need to maintain
                idx = ss.bisect_right((prices[index], float('Inf')))
                while idx < len(ss) and ss[idx][1] <= profits[index]:
                    ss.remove(ss[idx])
                ss.add((prices[index], profits[index]))

            return 
        left = [0] * len(prices) # store max profit before current index
        find(left, prices, profits) 
        right = [0] * len(prices) # store max profit after current index
        find(right, [-prices[i] for i in range(len(prices) - 1, -1, -1)], profits[::-1]) # in order use find function for set left
        right = right[::-1]
        res = -1
        for i in range(1, len(prices) - 1):
            if left[i] == 0 or right[i] == 0:
                continue
            res = max(res, left[i] + right[i] + profits[i])

        return res
   