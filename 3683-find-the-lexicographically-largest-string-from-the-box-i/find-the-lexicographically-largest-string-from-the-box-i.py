class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: return word
        char, idxarr, ans = word[0], [], ""
        for i in range(len(word) - 1, -1, -1):
            if word[i] >= char: char = word[i]; idxarr.append(i)
        return max([word[idx:len(word) - numFriends + idx + 1] for idx in idxarr])