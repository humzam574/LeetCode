class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = defaultdict(int)
        cons = defaultdict(int)
        for c in s:
            if c in {'a', 'e', 'i', 'o', 'u'}:
                vowels[c]+=1
            else:
                cons[c]+=1

        high = 0
        highvow = 0
        for k,v in vowels.items():
            if v > high:
                high = v
                highvow = v
        
        high = 0
        highcons = 'b'
        for v,k in cons.items():
            if k > high:
                high = k
                highcons = v
        
        return high+ highvow