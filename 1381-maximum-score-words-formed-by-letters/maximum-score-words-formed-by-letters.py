class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        freq = defaultdict(int)
        for l in letters:
            freq[l]+=1
        ans = 0
        # print(freq)
        for i in range(1, (2**n)+1):
            # print(bin(i)[2:])
            b = bin(i)[2:]
            b = ("0" * (n - len(b))) + b
            # print(b)
            curr = defaultdict(int)
            use = []
            for j,c in enumerate(b):
                if c == "1":
                    use.append(words[j])
            cont = True
            for word in use:
                for w in word:
                    curr[w]+=1
                    if curr[w] > freq[w]:
                        cont = False
                        break
            # print(curr)
            if not cont:
                continue
            # print(curr)
            
            val = 0
            for k, v in curr.items():
                val+=v*score[ord(k) - 97]
            # print(val)
            # print()
            ans = max(ans, val)
        return ans