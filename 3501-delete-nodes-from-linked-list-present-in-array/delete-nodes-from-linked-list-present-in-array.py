# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        while head and head.val in nums:
            head = head.next
        temp = head
        if not temp: return None
        while temp and temp.next:
            while temp.next and temp.next.val in nums:
                temp.next = temp.next.next
            temp = temp.next
        return head