class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        num_words = len(words)
        lengths = sorted(map(len, words), reverse=True)
        counts = Counter(chain(*words))
        odds = sum(count & 1 for count in counts.values())
        odds -= sum(length & 1 for length in lengths)
        trash = 0
        while odds > 0 and trash < num_words:
            odds -= lengths[trash] >> 1 << 1
            trash += 1
        return num_words - trash