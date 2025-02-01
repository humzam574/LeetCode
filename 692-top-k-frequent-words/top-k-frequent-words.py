class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict, freq, ans = Counter(words), defaultdict(list), []
        for key, v in dict.items(): freq[v].append(key)
        for key, v in freq.items(): freq[key].sort()
        for i in sorted(freq.keys(), reverse = True):
            arr = freq[i]
            if len(arr) > k:
                for item in arr[:k]: ans.append(item)
            else:
                for item in arr: ans.append(item)
            k -= len(arr)
            if k <= 0: break
        return ans