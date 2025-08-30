class Solution:
    def buildMatrix(self, k: int, rowconds: List[List[int]], colconds: List[List[int]]) -> List[List[int]]:
        #build a k x k square matrix
        
        #for rowconditions where each idx is [a,b]
        #a should be in a row that is striclty above where b appears
        
        #for colconditions where each idx is [c, d]
        #c should appear strictly left of d

        #topo sort from rows --> kahns
        #topo sort from cols --> kahns
        #construct and you're done! :)
        def kahns(rows):
            rowdeps = [0] * (k+1)
            rowmap = defaultdict(list)
            if rows:
                for a,b in rowconds:
                    #a is before b
                    #b depends on a
                    rowdeps[b]+=1
                    rowmap[a].append(b)
            else:
                for a,b in colconds:
                    #a is before b
                    #b depends on a
                    rowdeps[b]+=1
                    rowmap[a].append(b)
            
            #rowsort = [0] * k
            rowsort = []
            # print(rowdeps)
            # print(rowmap)

            dq = deque()
            for i,v in enumerate(rowdeps):
                if i == 0:
                    continue
                if v == 0:
                    dq.append(i)
            
            #ptr = 0
            while dq:
                n = dq.popleft()
                #rowsort[ptr] = n
                rowsort.append(n)
                #ptr+=1
                for nb in rowmap[n]:
                    rowdeps[nb]-=1
                    if rowdeps[nb] == 0:
                        dq.append(nb)
            if len(rowsort) != k:
                return [-1]
            return rowsort
        
        rows = kahns(True)
        cols = kahns(False)

        if rows == [-1] or cols == [-1]:
            return []
        
        indices = defaultdict(list)
        for i,c in enumerate(rows):
            indices[c].append(i)
        for i,c in enumerate(cols):
            indices[c].append(i)
        
        ans = [[0] * k for _ in range(k)]

        for k,v in indices.items():
            ans[v[0]][v[1]] = k
        return ans