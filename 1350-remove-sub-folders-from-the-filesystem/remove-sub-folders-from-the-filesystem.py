class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        #classic trie problem
        #paths = [None] * 27
        paths = {}
        # print('/a/b/ca/d'.split('/'))
        for path in folder:
            node = paths
            for ch in path.split('/'):
                # if ch != '/':
                    # idx = ord(ch) - ord('a')
                    # if not node[idx]:
                    #     node[idx] = [None] * 27
                    # node = node[idx]
                if ch:
                    if ch not in node:
                        node[ch] = {}
                    node = node[ch]
            node[0] = 1
        # for p in paths:
        #     print(p)
        #     print()
        # print(paths)
        self.ans = []
        def dfs(node, curr):
            if 0 in node:
                self.ans.append(curr)
                return
            oa = ord('a')
            # for i in range(26):
            #     if node[i]:
            #         curr += ("/" + chr(i+oa))
                    
            #         print(curr)
            #         dfs(node[i], curr)
            #         curr = curr[:-2]
            for key in node.keys():
                if key != 0:
                    curr += "/" + key
                    # print(key)
                    dfs(node[key], curr)
                    curr = curr[:-(1+len(key))]
        dfs(paths, "")
        return self.ans