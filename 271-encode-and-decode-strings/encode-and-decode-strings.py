class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        lst = []
        for word in strs:
            ans = ["" for _ in range(len(strs))]
            for c in word:
                ans.append(chr((ord(c) + 1) % 256))
            lst.append(''.join(ans))
        return lst
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        lst = []
        
        for word in s:
            ans = ["" for _ in range(len(s))]
            for c in word:
                ans.append(chr((ord(c) - 1) % 256))
            lst.append(''.join(ans))
        return lst
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))