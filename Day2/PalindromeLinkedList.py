# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        find_middle_node=self.firstHalf(head)
        second_half_reverse=self.reverseLinkedList(find_middle_node.next)

        status=True
        start=head
        cont=second_half_reverse
        while status and cont is not None:
            if start.val!=cont.val:
                status=False
            start=start.next
            cont=cont.next
        find_middle_node.next=self.reverseLinkedList(second_half_reverse)
        return status
    def firstHalf(self,head):
        first=head
        second=head
        while second.next is not None and second.next.next is not None:
            first=first.next
            second=second.next.next
        return first
    def reverseLinkedList(self,head):
        prev=None
        curr=head
        while curr is not None:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        return prev


        