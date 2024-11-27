class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        middle = -1 if len(palindrome) % 2 == 0 else len(palindrome) // 2
        for i,char in enumerate(palindrome):
            if char != "a" and i != middle:
                return palindrome[:i] + "a" + palindrome[i+1:]
        return "" if len(palindrome) == 1 else palindrome[:len(palindrome) - 1] + "b"