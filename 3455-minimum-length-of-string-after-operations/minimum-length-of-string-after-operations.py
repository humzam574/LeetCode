class Solution:
    def minimumLength(self, s: str) -> int:
        return sum(2 - int(n % 2) for n in Counter(s).values())