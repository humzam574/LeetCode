class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def search(v):
            drop = ord('a')
            val = 0
            high = int(26 ** (v-1))
            for i in range(v):
                val = val*26 + (ord(s[i]) - drop) 
            seen = {val}
            for i in range(v, len(s)):
                # Remove leftmost character
                val = val - (ord(s[i-v]) - drop) * high
                # Shift left and add new character
                val = val * 26 + (ord(s[i]) - drop)
                
                # Check if we've seen this hash before
                if val in seen:
                    return s[i-v+1:i+1]
                seen.add(val)
            return ""
        l, r = 0, len(s) - 1
        st = set()
        if len(set(s)) == 1:
            return s[:-1]
        curr = ""
        high = search(1)
        if high:
            l+=1
        while l < r:
            m = (l + r) // 2
            curr = search(m)
            if curr:
                high = curr
                l = m + 1
            else:
                r = m
            #print(str(l) + " " + str(r) + " " + str(m))
        return high