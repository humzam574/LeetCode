from collections import defaultdict
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        t1 = defaultdict(list)
        t2 = defaultdict(list)
        m = 0
        n = 0

        for e1, e2 in edges1:
            t1[e1].append(e2)
            t1[e2].append(e1)
            m = max(m, e1, e2)
        for e1, e2 in edges2:
            t2[e1].append(e2)
            t2[e2].append(e1)
            n = max(n, e1, e2)

        def dfs(node, parent, tree):
            farthest_node, max_dist = node, 0
            if tree == 1:
                for neighbor in t1[node]:
                    if neighbor != parent:
                        next_node, dist = dfs(neighbor, node, tree)
                        dist += 1
                        if dist > max_dist:
                            farthest_node, max_dist = next_node, dist
            else:
                for neighbor in t2[node]:
                    if neighbor != parent:
                        next_node, dist = dfs(neighbor, node, tree)
                        dist += 1
                        if dist > max_dist:
                            farthest_node, max_dist = next_node, dist
            return farthest_node, max_dist

        def find_diameter(tree, max_node):
            farthest_node, _ = dfs(0, -1, tree)
            _, diameter = dfs(farthest_node, -1, tree)
            return diameter

        dep1 = find_diameter(1, m + 1)
        dep2 = find_diameter(2, n + 1)

        return max(dep1, dep2, int(dep1 / 2 + 0.5) + int(dep2 / 2 + 0.5) + 1)
