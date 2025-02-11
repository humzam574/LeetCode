class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stacc = []
        n = len(part)
        for char in s:
            stacc.append(char)
            # if len(stacc) >= n:
            #     print(''.join(stacc[-n:]))
            while len(stacc) >= n and ''.join(stacc[-n:]) == part:
                for i in range(n):
                    stacc.pop()
        return ''.join(stacc)
