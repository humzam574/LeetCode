class Solution:
    def doesAliceWin(self, s: str) -> bool:
        #if theres an even amount, alice will pick an odd chunk and bob loses

        #if there is a odd amount, alice picks an odd amount and the rest is bob which is even
        #now there is an even amount and bob takes it all

        count = 0
        for c in s:
            if c in {'a', 'e', 'i', 'o', 'u'}:
                return True
        # if not count:
        #     return False
        return False