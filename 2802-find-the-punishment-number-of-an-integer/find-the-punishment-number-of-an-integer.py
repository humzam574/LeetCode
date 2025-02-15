class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0
        def bt(remaining_string: str, remaining_target: int) -> bool:
            if len(remaining_string) == 0:
                return remaining_target == 0

            if int(remaining_string) == remaining_target:
                return True

            for j in range(1, len(remaining_string)):
                if bt(remaining_string[j:], remaining_target - int(remaining_string[:j])):
                    return True
            return False
        for i in range(1, n+1):
            if bt(str(i*i), i):
                ans+=i*i
        return ans