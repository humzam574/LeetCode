class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k
        curr = blocks[:r].count("W")
        ans = curr
        while r < len(blocks):
            if blocks[l] == "W":
                curr -= 1
            l += 1
            if blocks[r] == "W":
                curr += 1
            r += 1
            ans = min(ans, curr)
        return ans
