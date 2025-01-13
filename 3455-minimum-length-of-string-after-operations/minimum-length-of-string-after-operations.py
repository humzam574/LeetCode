class Solution:
    def minimumLength(self, s):
        ans = 0
        for ch in {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}: count = s.count(ch); ans += (1 if count & 1 else 2 if count != 0 else 0)
        return ans