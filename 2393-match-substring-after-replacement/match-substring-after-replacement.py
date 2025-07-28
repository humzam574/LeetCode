class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        maps = defaultdict(set)
        for a, b in mappings:
            #maps[a].add(b)
            maps[b].add(a)
        l = 0
        for r in range(len(sub), len(s)+1):
            #code code code
            pos = True
            for i in range(l, r):
                if not (s[i] == sub[i - l] or sub[i - l] in maps[s[i]]):
                    pos = False
                    break
            if pos:
                return True
            l+=1
        return False
