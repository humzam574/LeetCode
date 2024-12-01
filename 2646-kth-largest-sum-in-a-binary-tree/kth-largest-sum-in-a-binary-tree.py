class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        h, q = [], [root]
        while q:
            temp, sm = [], 0
            for i in q:
                sm += i.val
                if i.left: temp.append(i.left)
                if i.right: temp.append(i.right)
            if len(h) < k: heappush(h, sm)
            elif sm > h[0]:
                heappop(h)
                heappush(h, sm)
            q = temp
        return -1 if len(h) < k else h[0]