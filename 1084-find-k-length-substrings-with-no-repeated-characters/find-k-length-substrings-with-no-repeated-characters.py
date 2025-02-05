class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s): return 0
        chars = set()
        left = 0
        count = 0
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            if right - left + 1 == k:
                count += 1
                chars.remove(s[left])
                left += 1
        return count