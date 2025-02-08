class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        print(Counter(word).values())
        #two options
        #decreasing the high occurrences
        #or cutting the low occurrences

        #calculate both options
        dict = Counter(word)
        arr = sorted(dict.values())
        print(arr)
        #try cutting 0 all the way to len(arr)
        l = 0
        r = 0
        currl = 0
        curr = 0
        ans = inf
        for i in range(len(arr)):
            if i > 0:
                currl += arr[i - 1]
            l = i
            r = len(arr) - 1
            curr = currl
            for j in range(i + 1, len(arr)):
                if arr[j] - arr[i] >= k:
                    break
            if l == len(arr) - 1:
                ans = min(ans, currl)
            elif j < len(arr):
                curr += max(sum(arr[j:]) - (arr[i] + k)*max(len(arr) - j, 0), 0)
                ans = min(ans, curr)
            # if ans == 6:
            #     print(i)
            #     print(j)
        return ans



        #minimum cuts and movements to make arr[-1] - arr[0] <= k