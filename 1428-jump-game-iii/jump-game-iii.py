class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        dp = [False] * n
        visited = set()
        def dfs(idx, dep):
            if idx < 0 or idx >= n: return False
            if arr[idx] == 0: return True
            if idx in visited: return False
            visited.add(idx)
            return dfs(idx - arr[idx], dep + 1) or dfs(idx + arr[idx], dep + 1)
        return dfs(start, 0)