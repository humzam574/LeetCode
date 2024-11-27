class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        ans = ""
        middle = -1
        if len(palindrome) == 1:
            return ""
        if (len(palindrome) % 2 == 1):
            middle = len(palindrome) // 2
        for i,char in enumerate(palindrome):
            if i == middle:
                continue
            if char != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]
        return palindrome[:len(palindrome) - 1] + "b"