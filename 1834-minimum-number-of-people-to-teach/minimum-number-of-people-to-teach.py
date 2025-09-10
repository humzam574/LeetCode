class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        #make an o(n^2) approach
        #create an adjacency for every friend combo which doesnt know eachothers language
        #turn the languages array into a an array of sets

        m = len(languages)
        for i in range(m):
            languages[i] = set(languages[i])
        
        arr = []
        for a,b in friendships:
            if languages[a-1].intersection(languages[b-1]):
                continue
            arr.append([a,b])
        
        print(arr)
        ans = inf
        #for language 1 through n, go through the pairs and see who needs to be taught
        for i in range(1, n+1):
            taught = set()
            for a,b in arr:
                if (a in taught or i in languages[a-1]) and (b in taught or i in languages[b-1]):
                    continue
                if i not in languages[a-1]:
                    taught.add(a)
                if i not in languages[b-1]:
                    taught.add(b)
            ans = min(ans, len(taught))
        return ans
            