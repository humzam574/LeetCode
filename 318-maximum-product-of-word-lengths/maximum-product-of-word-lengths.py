class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lengths = defaultdict(int)

        for word in words:
            mask = 0

            chars = set(c for c in word)

            for c in chars:
                mask += 1 << ord(c) - ord('a')
            
            lengths[mask] = max(lengths[mask], len(word))
        
        maxProduct = 0


        for m1, l1 in lengths.items():
            for m2, l2 in lengths.items():
                if m1 & m2 == 0:
                    maxProduct = max(maxProduct, l1 * l2)
        
        return maxProduct