class Solution:
    def smallestNumber(self, n: int) -> int:
        if n == 1:
            return 1
        if n <= 3:
            return 3
        if n <= 7:
            return 7
        if n <= 15:
            return 15
        if n <= 31:
            return 31
        if n <= 63:
            return 63
        if n <= 127:
            return 127
        if n <= 255:
            return 255
        if n <= 511:
            return 511
        return 1023