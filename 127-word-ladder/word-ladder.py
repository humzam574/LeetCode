from collections import defaultdict
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build intermediate words dict --- ["*ot": [hot, dot, lot]]
        wordsLength = len(wordList)

        intermediate_words = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                intermediate = word[:i] + "*" + word[i+1:]
                intermediate_words[intermediate].append(word)
        print(intermediate_words)

        # queue
        queue = deque()
        queue.append((beginWord, 1))

        visited = set()
        visited.add(beginWord)

        while queue:
            word, level = queue.popleft()

            for i in range(len(word)):
                intermediate = word[:i] + "*" + word[i+1:]
                for neighbor in intermediate_words[intermediate]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level+1))
        return 0
        
        