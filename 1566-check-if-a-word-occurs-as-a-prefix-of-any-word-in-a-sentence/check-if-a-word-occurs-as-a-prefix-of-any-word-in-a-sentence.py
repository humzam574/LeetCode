class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split(' ')
        size = len(searchWord)
        for i,word in enumerate(arr):
            if len(word) >= size:
                if word[:size] == searchWord:
                    return i+1
        return -1