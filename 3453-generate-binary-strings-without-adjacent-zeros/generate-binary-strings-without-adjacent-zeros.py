class Solution:
    def validStrings(self, n: int) -> List[str]:
        self.ans = []
        def dfs(curr):
            if len(curr) == n:
                self.ans.append(curr)
                return
            if not curr or curr[-1] == "1":
                dfs(curr + "0")
            dfs(curr + "1")
        dfs("")
        return self.ans