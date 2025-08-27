class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        #get all the unique i,j combos to make before and after phrases
        ans = set()
        starts = defaultdict(list)
        ends = defaultdict(list)

        for phr in phrases:
            sti = phr.find(' ')
            startexists = True
            if sti == -1:
                startexists = False
                sti = len(phr)
            start = phr[:sti]
            ndi = -1
            for i, c in enumerate(phr):
                if c == ' ':
                    ndi = i
            end = phr[ndi+1:]
            # print(phr)
            # print(start)
            # print(end)
            # print()
            for val in starts[end]:
                # print("adding on " + phr)
                if val:
                    ans.add(phr + " " + val)
                else:
                    ans.add(phr)
            for val in ends[start]:
                # print("adding on " + phr)
                if val:
                    ans.add(val + " " + phr)
                else:
                    ans.add(phr)
            if startexists:
                starts[start].append(phr[sti+1:])
            else:
                starts[start].append('')
            if ndi != -1:
                ends[end].append(phr[:ndi])
            else:
                ends[end].append('')
        # print(starts)
        # print()
        # print(ends)
        # print()
        # print(ans)
        return sorted(list(ans))