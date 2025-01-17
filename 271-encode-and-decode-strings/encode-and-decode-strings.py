class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for i in strs:
            res+=str(len(i))
            res+="#"
            res+=i
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        t = 0
        l = len(s)
        while t < l:
            end = t
            while s[end] != "#":
                end+=1
            num = int(s[t:end])
            t = end+1
            res.append(s[t:t+num])
            t+=num
        return res