class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for s in strings:
            #generate a delta
            delta = ord(s[0])
            arr = []
            for c in s:
                val = ord(c) - delta
                if val < 0:
                    val = 26 + val
                arr.append(val)
            #print(arr)
            freq[tuple(arr)].append(s)
        return list(freq.values())