class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        # If the length difference is more than 1, return False immediately
        if abs(m - n) > 1:
            return False

        # Ensure s is the shorter string (for convenience)
        if m > n:
            s, t = t, s  # Swap so that s is always shorter or equal
            m, n = n, m

        for i in range(len(s)):  # Traverse the shorter string
            if s[i] != t[i]:  # Found the first difference
                # If lengths are equal, check replacement
                if m == n:
                    return s[i+1:] == t[i+1:]  # Check remaining substring match

                # If lengths differ, check if skipping one character in t fixes it
                return s[i:] == t[i+1:]

        # If no differences found, check for the case where t has one extra character
        return m + 1 == n