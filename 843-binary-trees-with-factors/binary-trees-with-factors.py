MOD = 1_000_000_007


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        dp = {num: 1 for num in arr}

        s = set(arr)
        for i in range(n):
            for j in range(i + 1):
                curr = arr[i] * arr[j]
                if curr > arr[-1]:
                    break

                if curr in dp:
                    multi = 1 if i == j else 2
                    dp[curr] = (dp[curr] + dp[arr[i]] * dp[arr[j]] * multi) % MOD

        return sum(dp.values()) % MOD