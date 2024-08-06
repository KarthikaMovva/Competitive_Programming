# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        else:
            first=head
            second=head.next
            while first!=second:
                if not second or not second.next:
                    return False
                else:
                    first=first.next
                    second=second.next.next
            return True
        