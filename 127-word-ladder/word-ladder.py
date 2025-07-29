class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        def offbyone(a, b):
            off = 0
            for i in range(n):
                if a[i] != b[i]:
                    off+=1
            return off == 1
        dq = deque()
        unvisited = set(wordList)
        #unvisited.add(endWord)
        dq.append((beginWord, 1))
        while dq:
            # print(dq)
            word, dep = dq.popleft()
            skip = set()
            for w in unvisited:
                if offbyone(w, word):
                    if w == endWord:
                        return dep+1
                    # unvisited.remove(w)
                    skip.add(w)
                    dq.append((w, dep+1))
            for item in skip:
                unvisited.remove(item)
        return 0
        