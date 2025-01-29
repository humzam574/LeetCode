class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        head = list(range(len(edges) + 1))
        def find(node):
            if head[node] != node:
                head[node] = find(head[node])
            return head[node]
        
        for n1, n2 in edges:
            r1, r2 = find(n1), find(n2)
            if r1 == r2:
                return [n1, n2]
            head[r2] = r1