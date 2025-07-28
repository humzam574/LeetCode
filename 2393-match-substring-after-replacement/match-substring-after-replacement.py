class Solution:
    def matchReplacement(
        self, 
        s: str, 
        sub: str, 
        mappings: List[List[str]]
    ) -> bool:
        empty, m, ss = [], {}, set(s)

        if len(sub) > len(s):
            return False
        elif sub in s:
            return True

        for mapping in mappings:
            if mapping[1] not in ss:
                continue

            if mapping[0] not in m:
                m[mapping[0]] = []

            m[mapping[0]].append(mapping[1])

        if not m:
            return False
        
        for i in range(len(s) - len(sub), -1, -1):
            for j, c in enumerate(s[i : i + len(sub)]):
                if c != sub[j] and c not in m.get(sub[j], empty):
                    break
            else:
                return True
            
        return False