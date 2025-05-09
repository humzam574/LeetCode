class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = defaultdict(int)
        for r in responses:
            visited = set()
            for word in r:
                if word not in visited:
                    visited.add(word)
                    count[word]+=1
        arr = [[a, b] for a,b in count.items()]
        arr.sort(reverse = True, key = lambda x : x[1])
        ans = [arr[0]]
        i = 1
        #print(arr)
        while i < len(arr) and count[arr[i][0]] == arr[0][1]:
            ans.append(arr[i])
            i+=1
        ans.sort(key = lambda x : x[0])
        #print(ans)
        return ans[0][0]