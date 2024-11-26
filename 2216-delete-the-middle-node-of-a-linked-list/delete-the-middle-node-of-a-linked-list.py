# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head.next
        slow = ListNode()
        slow.next = head
        if not fast:
            return None
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head