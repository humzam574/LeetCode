class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        sec = Counter(secret)
        skip = set()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                skip.add(i)
                sec[secret[i]]-=1
                bulls+=1
        
        for i,c in enumerate(guess):
            if i in skip:
                continue
            if c in sec and sec[c] > 0:
                sec[c]-=1
                cows+=1
        
        return str(bulls) + "A" + str(cows) + "B"