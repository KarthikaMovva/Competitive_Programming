
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummyNode = ListNode(0) 
        dummyNode.next = head
        firstNode=dummyNode
        secondNode=dummyNode
        
        for _ in range(n):
            firstNode = firstNode.next

        while firstNode.next:
            firstNode = firstNode.next
            secondNode = secondNode.next
        secondNode.next = secondNode.next.next
        
        return dummyNode.next
        