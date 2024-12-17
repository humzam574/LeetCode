class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = [[a, "a"], [b, "b"], [c, "c"]]
        arr.sort(reverse = True, key = lambda x : x[0])
        curr = arr[0][1]
        arr[0][0] -= 1
        i  = 0
        while i < len(arr):
            if arr[i][0] == 0:
                arr.pop(i)
                i-=1
            i+=1
        ans = curr
        while len(arr) > 0:
            #print(arr)
            #print(ans)
            arr.sort(reverse = True, key = lambda x : x[0])
            idx = 0
            if arr[0][1] == curr[-1]:
                while idx < len(arr) and arr[idx][1]*2 == curr:
                    idx+=1
                if idx == len(arr):
                    return ans
            if arr[idx][1] == curr[-1]:
                curr+=arr[idx][1]
            else:
                curr = arr[idx][1]
            ans+=arr[idx][1]
            arr[idx][0]-=1
            if arr[idx][0] == 0:
                arr.pop(idx)
        return ans
            