class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        t1, t2 = defaultdict(list), defaultdict(list)
        for e1, e2 in edges1: t1[e1].append(e2); t1[e2].append(e1)
        for e1, e2 in edges2: t2[e1].append(e2); t2[e2].append(e1)
        def dfs(node, parent, tree):
            farthest_node, max_dist = node, 0
            for neighbor in tree[node]:
                if neighbor != parent:
                    next_node, dist = dfs(neighbor, node, tree)
                    if dist + 1 > max_dist: farthest_node, max_dist = next_node, dist + 1
            return farthest_node, max_dist
        dep1, dep2 = dfs(dfs(0, None, t1)[0], None, t1)[1], dfs(dfs(0, None, t2)[0], None, t2)[1]
        return max(dep1, dep2, ceil(dep1 / 2) + ceil(dep2 / 2) + 1)
