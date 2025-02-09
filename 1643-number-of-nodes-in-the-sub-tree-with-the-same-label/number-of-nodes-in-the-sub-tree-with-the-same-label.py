class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.graph = [[] for i in range(n)]
        self.ans = [0] * n
        for a, b in edges:
            self.graph[a].append(b)
            self.graph[b].append(a)
        #print(self.graph)
        def dfs(curr, prev):
            if not len(self.graph[curr]):
                arr = [0] * 26
                idx = ord(labels[curr]) - 97
                arr[idx] += 1
                self.ans[curr] += arr[idx]
            else:
                arr = [0] * 26
                for x in self.graph[curr]:
                    if x == prev:
                        continue
                    arr = [a + b for a, b in zip(arr, dfs(x, curr))]
                idx = ord(labels[curr]) - 97
                arr[idx] += 1
                self.ans[curr] += arr[idx]
            # print(curr)
            # print(arr)
            # print()
            return arr
        dfs(0, None)
        return self.ans