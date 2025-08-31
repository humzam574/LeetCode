# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        counts = defaultdict(int)
        curr = head
        while curr:
            counts[curr.val]+=1
            curr = curr.next

        rems = set()
        for k,v in counts.items():
            if v > 1:
                rems.add(k)
        # print(rems)
        while head and head.val in rems:
            head = head.next
        
        curr = head
        while curr and curr.next:
            while curr and curr.next and curr.next.val in rems:
                curr.next = curr.next.next
            curr = curr.next
        return head