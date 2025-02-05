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
        if not root:
            return None
        
        lev = root
        
        while lev:
            dummy = Node(0)
            child = dummy
            
            while lev:
                if lev.left:
                    child.next = lev.left
                    child = child.next
                    
                if lev.right:
                    child.next = lev.right
                    child = child.next
                    
                lev = lev.next
            lev = dummy.next
            
        return root