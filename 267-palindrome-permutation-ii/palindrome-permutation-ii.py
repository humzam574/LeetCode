class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        count = Counter(s)
        odds = 0
        for v in count.values():
            if v % 2:
                odds += 1
        if odds > 1:
            return []
            
        mid = ''
        half = []
        for c, v in count.items():
            for i in range(v//2):
                half.append(c)
            if v % 2:
                mid = c
                
        result = set()
        for p in permutations(half):
            half_str = ''.join(p)
            palindrome = half_str + mid + half_str[::-1]
            result.add(palindrome)
            
        return list(result)