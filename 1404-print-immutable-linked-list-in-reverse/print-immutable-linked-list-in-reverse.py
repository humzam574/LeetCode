# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.getNext()
        
        for i in range(len(nodes)-1, -1, -1):
            nodes[i].printValue()