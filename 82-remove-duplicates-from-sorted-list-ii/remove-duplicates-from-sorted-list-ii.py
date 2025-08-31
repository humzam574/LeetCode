# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        push = False
        cont = True
        while cont:
            while head and head.next and head.val == head.next.val:
                push = True
                head = head.next
            if push and head:
                head = head.next
            
            else:
                cont = False
            push = False
        curr = head
        while curr and curr.next and curr.next.next:
            cont = True
            while cont:
                rem = -101
                if curr and curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                    rem = curr.next.val
                while curr and curr.next and curr.next.val == rem:
                    curr.next = curr.next.next
                if rem == -101:
                    cont = False
            curr = curr.next
        return head