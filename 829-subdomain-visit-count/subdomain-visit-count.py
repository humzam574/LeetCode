class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict = defaultdict(int)
        for d in cpdomains:
            if d.count('.') == 2:
                one = two = three = ""
                l = 0
                m = 0
                r = 0
                for i, c in enumerate(d):
                    if c == " ":
                        l = i
                    elif c == ".":
                        if m == 0:
                            m = i
                        else:
                            r = i
                            break
                one = d[r + 1:]
                two = d[m + 1:]
                three = d[l + 1:]
                count = int(d[:l])
                dict[one] += count
                dict[two] += count
                dict[three] += count
            else:
                one = two = ""
                l = 0
                r = 0
                for i, c in enumerate(d):
                    if c == " ":
                        l = i
                    elif c == ".":
                        r = i
                        break
                count = int(d[:l])
                one = d[l+1:]
                two = d[r+1:]
                dict[two]+=count
                dict[one]+=count
        
        ans = []
        for k, v in dict.items():
            temp = str(v) + " " + k
            ans.append(temp)
        return ans