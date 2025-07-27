def merge(a,b):
    if b in a:
        return a
    for i in range(min(len(a),len(b)), 0 ,-1):
         if a[-i:] == b[:i]:
            return a+b[i:]
    return a+b
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        candidates = []
        candidates.append(merge(merge(a,b),c))    
        candidates.append(merge(merge(b,a),c))    
        candidates.append(merge(merge(a,c),b))    
        candidates.append(merge(merge(c,a),b))    
        candidates.append(merge(merge(b,c),a))    
        candidates.append(merge(merge(c,b),a))
        ans = candidates[0]
        #return candidates
        for s in candidates:
            if len(s)<len(ans) or (len(s) == len(ans) and s<ans):
                ans = s
        return ans