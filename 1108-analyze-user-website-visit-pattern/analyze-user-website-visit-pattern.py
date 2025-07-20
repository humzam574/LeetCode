class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        #for each user create an array of their website visits
        #make a dict key username value arr
        #each value in arr is [website, timestamp]
        #then sort by timestamp and chop it off
        #then make a freq dict
        visits = defaultdict(list)
        n = len(username)
        for i in range(n):
            ign = username[i]
            ts = timestamp[i]
            wb = website[i]
            visits[ign].append([wb, ts])
        # for k, v in visits.items():
        #     print("k: ", end = "")
        #     print(k)
        #     print("v: ", end = "")
        #     print(v)
        #     print()
        # print("ON TO FREQ")
        # print()
        # print()
        freq = defaultdict(int)
        for k, v in visits.items():
            if len(v) < 3:
                continue
            v.sort(key = lambda x : x[1])
            v = [a[0] for a in v]
            # for i in range(len(v) - 2):
            #     freq[tuple(v[i:i+3])]+=1
            st = set()
            ln = len(v)
            for i in range(ln):
                for j in range(i + 1, ln):
                    for k in range(j + 1, ln):
                        # freq[(v[i], v[j], v[k])]+=1
                        st.add((v[i], v[j], v[k]))
            for val in st:
                freq[val]+=1
        # for k, v in freq.items():
        #     print("k: ", end = "")
        #     print(k)
        #     print("v: ", end = "")
        #     print(v)
        #     print()
        val = 0
        ans = ""
        for k, v in freq.items():
            if v > val:
                val = v
                ans = k
            elif v == val:
                # if ''.join(ans) > ''.join(k):
                #     ans = k
                if ans[0] > k[0]:
                    ans = k
                elif ans[0] == k[0]:
                    if ans[1] > k[1]:
                        ans = k
                    elif ans[1] == k[1]:
                        if ans[2] > k[2]:
                            ans = k
        return ans