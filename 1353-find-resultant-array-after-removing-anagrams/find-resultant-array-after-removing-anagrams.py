class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        stack = []

        stack.append(''.join(sorted(words[0])))
        res.append(words[0])

        for i in range(1, len(words)):
            curr = ''.join(sorted(words[i]))
            if stack[-1] != curr:
                stack.append(curr)
                res.append(words[i])
        return res