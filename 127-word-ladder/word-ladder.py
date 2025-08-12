# import atexit; atexit.register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        def search(curr):
            start = list(curr)
            curr = list(curr)
            ans = []
            for i in range(len(start)):
                for char in range(ord('a', ord('z')+1)):
                    char = chr(char)
                    if char == start[i]:
                        continue
                    curr[i] = char
                    temp = ''.join(curr)
                    if temp in wordList:
                        ans.append(temp)
                curr[i] = start[i]
            return ans
        
        prev = set()
        dq = deque()
        dq.append((beginWord, 1))
        while dq:
            curr, dep = dq.popleft()
            if curr == endWord:
                return dep
            prev.add(curr)
            start = list(curr)
            curr = list(curr)
            for i in range(len(start)):
                for char in range(ord('a'), ord('z')+1):
                    char = chr(char)
                    if char == start[i]:
                        continue
                    curr[i] = char
                    temp = ''.join(curr)
                    if temp in wordList and temp not in prev:
                        dq.append((temp, dep + 1))
                curr[i] = start[i]
        return 0


