
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        dummyNode = ListNode(0)
        dummyNode.next = head
        previous = dummyNode
        
        while True:
            kth_position = previous
            for i in range(k):
                kth_position = kth_position.next
                if not kth_position:
                    return dummyNode.next
            
            Nextgroup = kth_position.next
            prev, curr = previous.next, previous.next
            for j in range(k):
                pointer = curr.next
                curr.next = prev
                prev = curr
                curr = pointer
            
            pointer = previous.next  
            previous.next = prev  
            pointer.next = Nextgroup
            
            previous = pointer
            
        return dummyNode.next

        