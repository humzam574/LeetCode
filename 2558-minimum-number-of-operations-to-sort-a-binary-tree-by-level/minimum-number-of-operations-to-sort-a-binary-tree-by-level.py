# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append(root)
        ans = 0
        while dq:
            lev = []
            for i in range(len(dq)):
                if dq[0].left: dq.append(dq[0].left)
                if dq[0].right: dq.append(dq[0].right)
                lev.append(dq.popleft().val)
            dict = {num : idx for idx, num in enumerate(lev)}
            srt = sorted((num, idx) for idx, num in enumerate(lev))  # Pair values with their original indices
            visited = [False] * len(lev)  # Keep track of visited elements

            for i in range(len(lev)):
                if visited[i] or srt[i][1] == i:  # Skip already visited or correctly placed elements
                    continue
                
                # Detect cycle
                cycle_length = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = srt[j][1]  # Move to the index of the current element in the sorted array
                    cycle_length += 1
                
                # Add swaps needed for this cycle
                if cycle_length > 1:
                    ans += cycle_length - 1
        return ans
                    