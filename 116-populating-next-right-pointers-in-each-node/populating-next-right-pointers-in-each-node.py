"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        if not root.right: return root
        dq = deque([root.left, root.right])
        while dq:
            print(dq)
            for i in range(len(dq) - 1):
                dq[0].next = dq[1]
                if dq[0].right:
                    dq.append(dq[0].left)
                    dq.append(dq[0].right)
                dq.popleft()
            if dq[0].right:
                    dq.append(dq[0].left)
                    dq.append(dq[0].right)
            dq.popleft()
        return root
