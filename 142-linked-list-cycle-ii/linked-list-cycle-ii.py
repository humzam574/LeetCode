# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dict = {}
        pos = 0
        while head:
            if head in dict:
                return head
            dict[head] = pos
            pos += 1
            head = head.next
        return None#-1