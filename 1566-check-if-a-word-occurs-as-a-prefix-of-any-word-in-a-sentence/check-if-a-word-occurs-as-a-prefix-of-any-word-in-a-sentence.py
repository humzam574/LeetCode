class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence, size = sentence.split(), len(searchWord)
        for i in range(len(sentence)):
            if len(sentence[i]) >= size and sentence[i][:size] == searchWord: return i+1
        return -1