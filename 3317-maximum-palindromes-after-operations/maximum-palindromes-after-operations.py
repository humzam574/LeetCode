class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        #make a counter dict of all the characters
        #find a way to greedily allocate
        #maybe for all the odd values subtract them depending on the number of odd length words there are
        #lets say you delete all the odd numbers
        #find a way to greedily allocate
        #first allocate the smallest words
        #which letters you pick doesn't matter i think
        ans = 0

        wlens = sorted([len(w) for w in words])

        counter = [0] * 26
        for w in words:
            for c in w:
                counter[ord(c) - 97]+=1
        
        odds = 0
        
        for i in range(26):
            if counter[i] % 2 == 1:
                odds+=1
                counter[i] -= 1
        i = 0
        #you have a counter for all the letters
        print("odds to remove: " + str(odds))
        print("wlens before odds: ", end = "")
        
        print(wlens)
        print(counter)
        print()
        while i < len(wlens) and odds > 0:
            if wlens[i] == 1:
                ans+=1
                odds-=1
                wlens[i] = 0
            elif wlens[i] % 2 == 1:
                odds-=1
                wlens[i] -= 1
            i+=1
        # print(counter)
        # cntr = []
        # for num in counter:
        #     if num != 0:
        #         cntr.append(num)
        # print(cntr)
        rem = sum(counter)
        print(rem)
        print(wlens)
        print(counter)
        i = 0
        wlens2 = []
        for num in wlens:
            if num != 0:
                wlens2.append(num)
        while rem > 0 and i < len(wlens2):
            rem-=wlens2[i]
            if rem >= 0:
                ans+=1
            i+=1
        return ans