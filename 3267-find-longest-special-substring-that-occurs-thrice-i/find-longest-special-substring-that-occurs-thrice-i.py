class Solution:
    def maximumLength(self, s: str) -> int:
        def search():
            l, r = 0, 1
            val = 0
            while r < len(s):
                if s[r] != s[l]:
                    l = r
                else:
                    r+=1
                    val = max(val, r-l)
            return val
        ans = -1
        #solution doesnt have to be super efficient, maybe even O(n^3)
        #maybe make a hashmap counter
        #use two pointer to get the largest length substr, and get num occurrences
        #then find the num occurrences for substr of length - 1
        #and repeat until you hit 3
        
        high = search()
        for i in range(high, 0, -1):
            dict = defaultdict(int)
            l = 0
            r = i
            #print(i)
            possible = (len(set(s[l:r])) == 1)
            while r <= len(s):
                #print(dict)
                if (len(set(s[l:r])) == 1):
                    dict[s[l]]+=1
                    if dict[s[l]] == 3:
                        return i
                l+=1
                r+=1
            
        return -1