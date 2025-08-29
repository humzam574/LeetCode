class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # make adjacency matrix
        matrix = defaultdict(list)
        for u, v in adjacentPairs:
            matrix[u].append(v)
            matrix[v].append(u)

        root = None

        for key, value in matrix.items():
            if len(value) == 1:
                root = key
                break
        
        prev = None
        cur = root

        res = [root]

        while len(res) < len(matrix):
            for val in matrix[cur]:
                if val != prev:
                    res.append(val)
                    prev = cur
                    cur = val
                    break

        return res
        # find root

        # set prev = None, cur = root