class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        #adding tuple of each to sort on time
        comb = []
        for name,time,web in zip(username,timestamp,website):
            comb.append((name,time,web))
        comb.sort(key = lambda x : x[1])
        # amking a hashmap for each user
        table = defaultdict(list)
        for var in comb:
            table[var[0]].append(var[2])
        #identifying patterns
        patterns = defaultdict(int)
        for val in table.values():
            if len(val) >= 3:
                n = len(val)
                triplets = [(val[i],val[j],val[k]) for i in range(n) for j in range(i+1,n) for k in range(j+1,n)]
                for pat in set(triplets):
                    patterns[pat]+=1
        #getting the max len patterns
        maxval, res = 0,[]
        for key,val in patterns.items():
            if val > maxval or (val == maxval and list(key) < res):
                res = list(key)
                maxval = val
        # sorting to get the least lexographically val
        # res.sort()
        return res