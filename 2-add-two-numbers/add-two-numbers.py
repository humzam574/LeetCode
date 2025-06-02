# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #ex: 2->4->3, 5->6->4
        #becomes 342 + 465 = 807
        #return 7->0->8
        #add the two nodes, if overflows bring it back and add to the next
        #if next equals null and theres an overflow, create a new node with val = 1
        ans = ListNode()
        head = ans
        carry = 0

        while l1 or l2:
            if l1 and l2:
                add = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                add = l1.val + carry
                l1 = l1.next
            else:
                add = l2.val + carry
                l2 = l2.next
            carry = add // 10
            head.next = ListNode(add % 10)
            head = head.next
            #print(str(add) + " " + str(carry))
        if carry == 1:
            head.next = ListNode(1)
        

        return ans.next
        