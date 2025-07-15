class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        #for t, calculate the number of chars it will make for all letters a-z
        #calculate starting at z and then add one more iteration each time
        sim = deque([0] * 26)
        sim[0] = 1
        for i in range(t):
            sim.appendleft(0)
            if sim[26] != 0:
                var = sim[26]
                
                sim[0]+=var
                sim[1]+=var
            sim.pop()
        chars = set(s)
        high = max([ord(c) - ord('a') for c in s])
        keys = [0] * 26
        keys[0] = sum(sim)
        # print(high)
        for i in range(high):
            sim.appendleft(0)
            if sim[26] != 0:
                var = sim[26]
                
                sim[0]+=var
                sim[1]+=var
            sim.pop()
            keys[i+1] = sum(sim)
        ans = 0
        # print(keys)
        for c in s:
            ans+=keys[ord(c)-ord('a')]
            ans = ans % 1_000_000_007
        return ans % 1_000_000_007
