class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, queue, level_num = [], deque([root]), -1
        while queue:
            level, level_size, level_num = [], len(queue), level_num + 1
            for i in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if level_num % 2: level.reverse()
            res.append(level)
        return res