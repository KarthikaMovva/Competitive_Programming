
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head
        return new_head
        