class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = Counter(words)
        freq = defaultdict(list)
        for key, v in dict.items():
            freq[v].append(key)
        for key, v in freq.items():
            freq[key].sort()#reverse = True)
        f = sorted(freq.keys(), reverse = True)
        ans = []
        #print(f)
        #print(freq)
        for i in f:
            arr = freq[i]
            if len(arr) > k:
                #print(len(arr))
                #print(k)
                for item in arr[:k]:
                    ans.append(item)
                #ans = ans + arr[:k]
                k = 0
            else:
                #print("whole thing")
                for item in arr:
                    ans.append(item)
                k -= len(arr)
            
            #print(arr)
            #print(k)
            if k <= 0:
                break
        return ans