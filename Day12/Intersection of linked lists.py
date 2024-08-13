
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        ListpointerA = headA
        ListpointerB = headB
        
        while ListpointerA != ListpointerB:
            ListpointerA = ListpointerA.next if ListpointerA else headB
            ListpointerB = ListpointerB.next if ListpointerB else headA
        return ListpointerA
        