class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        right = [0]*n
        left = [0]*n
        count = 0
        start = False
        last = 0
        res = []

        # right
        for i in range(n-1, -1, -1):
            c = s[i]
            
            if not start and c == '*':
                right[i] = 0
                continue
            start = True

            if c == '|':
                last = count
            else: # c == '*'
                count += 1
            right[i] = last

        # left
        last = right[0]
        for i in range(n):
            c = s[i]
            if c == '|':
                last = right[i]
            left[i] = last

        for query in queries:
            s,e = query[0], query[1]
            val = right[s] - left[e]
            res.append(val if val >= 0 else 0)
        
        return res