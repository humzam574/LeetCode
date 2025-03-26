class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        #0, 1, 2, 3, 4, 5
        #prefix sum
        #1 2 3 5
        arr = []
        for row in grid:
            arr = arr + row
        arr.sort()
        post = sum(arr)# - arr[0]
        pre = 0
        n = len(arr)
        curr = 0
        ans = inf
        delta = arr[0] % x
        #print(arr)
        for i in range(n):
            if (arr[i] - delta) % x:
                return -1
            post -= arr[i]
            curr = (post - (n - i - 1) * arr[i]) // x + max(0, (arr[i]*i-pre)//x)
            #print(str(i) + " " + str(curr) + " " + str(pre) + " " + str(post))
            
            pre += arr[i]
            
            ans = min(ans, curr)
        return ans
        