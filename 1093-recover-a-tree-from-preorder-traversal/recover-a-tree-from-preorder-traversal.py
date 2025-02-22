# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        root = TreeNode()
        rightview = []
        #step one: process the string
        idx = 0
        #1-2--3--4-5--6--7
        #[0, 1], [1, 2], [2, 3], [2, 4], [1, 5], [2, 6], [2, 7]
        #1-2--3---4-5--6---7
        #[0, 1], [1, 2], [2, 3], [3, 4], [1, 5], [2, 6], [3, 7]
        curr = 0
        prev = 0
        n = ""
        process = []
        length = 1
        for i, char in enumerate(traversal):
            if char == "-":
                if traversal[i - 1].isdigit():
                    process.append((curr, int(n)))
                    length = max(length, curr)
                    n = ""
                    curr = 1
                else:
                    curr += 1
            else:
                n+=char
        process.append((curr, int(n)))
        length = max(length, curr)
        root = TreeNode(process[0][1])
        temp = root
        rv = [None] * (length + 1)
        rv[0] = temp
        for dep, val in process[1:]:
            t2 = TreeNode(val)
            rv[dep] = t2
            t3 = rv[dep - 1]
            if not t3.left:
                t3.left = t2
            else:
                t3.right = t2
        return root
