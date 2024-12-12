class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        #get half and get all permutations of it
        cnt = Counter(s)
        mid = None
        if len(s) % 2 == 1:
            for k, v in cnt.items():
                if v % 2 == 1:
                    mid = k
                    cnt[k] -= 1
                    break
        pm = []
        for k, v in cnt.items():
            if cnt[k] % 2: return []
            cnt[k] = cnt[k] // 2
            for i in range(cnt[k]):
                pm.append(k)
        print(pm)
        print(cnt)
        print(mid)
        ans = set()
        def perm(curr, left):
            if not left:
                ans.add(tuple(curr))
            for i, item in enumerate(left):
                perm(curr + [item], left[:i] + left[i+1:])
        perm([], pm)
        print(ans)
        ans = list(ans)
        for i,piece in enumerate(ans):
            temp = ''.join(piece)
            if mid:
                ans[i] = temp + mid + temp[::-1]
            else:
                ans[i] = temp + temp[::-1]
        return list(ans)