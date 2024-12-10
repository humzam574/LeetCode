class Solution:
    def maximumLength(self, s: str) -> int:
        #solution doesnt have to be super efficient, maybe even O(n^3)
        #maybe make a hashmap counter
        #use two pointer to get the largest length substr, and get num occurrences
        #then find the num occurrences for substr of length - 1
        #and repeat until you hit 3
        l, r, high = 0, 1, 0
        while r < len(s):
            if s[r] != s[l]: l = r
            else: r, high = r + 1, max(high, r - l + 1)
        for i in range(high, 0, -1):
            dict, l, r = defaultdict(int), 0, i
            while r <= len(s):
                if (len(set(s[l:r])) == 1):
                    if dict[s[l]] == 2: return i
                    dict[s[l]]+=1   
                l, r = l + 1, r + 1
        return -1