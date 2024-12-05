class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if (len(start) != len(target) or start.count('_') != target.count('_')): return False
        n, i, j = len(start), 0, 0
        while i < n or j < n:
            while i < n and start[i]  == '_': i += 1
            while j < n and target[j] == '_': j += 1
            if (i == n and j == n) or (i == n or j == n or start[i] != target[j]) or (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j): return i == n and j == n
            i, j = i + 1, j + 1
        return True