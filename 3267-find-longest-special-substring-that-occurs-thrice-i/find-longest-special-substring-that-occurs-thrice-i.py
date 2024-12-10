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
            curr = Counter(s[:i])
            if len(curr) == 1: dict[s[l]]+=1
            #print(curr)
            #print(dict)
            while r < len(s):
                
                curr[s[l]] -= 1
                if curr[s[l]] == 0:
                    del curr[s[l]]
                if s[r] in curr:
                    curr[s[r]]+=1
                else:
                    curr[s[r]] = 1
                #curr[s[r]] += 1
                
                
                #print(curr)
                #print(dict)
                l, r = l + 1, r + 1
                if (len(curr) == 1):
                    dict[s[l]]+=1
                    if dict[s[l]] == 3: return i
                #if r < len(s):
                
        return -1