# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        max_val = []
        cur_queue = deque()
        cur_queue.append(root)
        
        if not root:
            return max_val
        
        while cur_queue:
            n = len(cur_queue)
            cur_lvl_max = float('-inf')
            
            for _ in range(n):
                node = cur_queue.popleft()
                cur_lvl_max = max(cur_lvl_max, node.val)
                
                if node.left:
                    cur_queue.append(node.left)
                
                if node.right:
                    cur_queue.append(node.right)
                
            max_val.append(cur_lvl_max)        
        return(max_val)