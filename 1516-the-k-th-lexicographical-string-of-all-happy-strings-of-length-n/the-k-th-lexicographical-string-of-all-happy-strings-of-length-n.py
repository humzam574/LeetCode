class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * 2 ** (n-1): return ""
        happy = 'abc'
        bit_string = format(k-1, 'b').zfill(n+1)
        final_str = [happy[int(bit_string[:2], 2)]]
        for c in bit_string[2:]:
            if c == '0':
                if final_str[-1] == 'a': final_str.append('b')
                else: final_str.append('a')
            else:
                if final_str[-1] == 'c': final_str.append('b')
                else: final_str.append('c')
        return ''.join(final_str)