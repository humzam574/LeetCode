class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        l = 0
        if len(bank) == 1:
            return 0
        prev = bank[l].count('1')
        ans = 0
        for r in range(1, len(bank)):
            count = bank[r].count('1')
            if count != 0:
                ans+=(prev*count)
                prev = count
            # print(ans)
        return ans