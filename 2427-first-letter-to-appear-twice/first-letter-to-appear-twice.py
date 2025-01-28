class Solution:
    def repeatedCharacter(self, s: str) -> str:
        exist = set()
        for char in s:
            if char in exist:
                return char
            else:
                exist.add(char)