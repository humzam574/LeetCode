class Solution:
    def permute(self, n: int) -> List[List[int]]:
        #observations:
        #if n is odd, there are x+1 odds and x evens, so the odds are at the ends
        #if n is even, you can swap
        #use a dfs?

        self.ans = []
        def dfs(curr, rem):
            if not rem:
                self.ans.append(curr)
            ty = curr[-1] % 2
            arr = sorted(list(rem))
            for num in arr:
                if num % 2 != ty:
                    rem.remove(num)
                    dfs(curr + [num], rem)
                    rem.add(num)
            #code
        starter = {i for i in range(1, n + 1)}
        if n % 2 == 1:
            for x in range(1, n + 1, 2):
                starter.remove(x)
                dfs([x], starter.copy())
                starter.add(x)
        else:
            for x in range(1, n + 1):
                
                starter.remove(x)
                dfs([x], starter.copy())
                starter.add(x)
        return self.ans