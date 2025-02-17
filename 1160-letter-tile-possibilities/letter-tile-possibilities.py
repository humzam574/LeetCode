class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        #do a dfs with a length goal, curr, memo
        self.memo = set()
        def dfs(length, curr, rem):
            # if curr in self.memo:
            #     return
            if len(curr) == length:
                self.memo.add(curr)
                return
            for item in rem.keys():
                if rem[item] == 0:
                    continue
                curr = curr + item
                rem[item] -= 1
                dfs(length, curr, rem.copy())
                rem[item] += 1
                curr = curr[:len(curr) - 1]
        for i in range(1, len(tiles) + 1):
            dfs(i, "", Counter(tiles))
            #print(self.memo)
        return len(self.memo)