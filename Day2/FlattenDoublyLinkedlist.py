# """
# # Definition for a Node.
# class Node(object):
#     def __init__(self, val, prev, next, child):
#         self.val = val
#         self.prev = prev
#         self.next = next
#         self.child = child
# """

class Solution(object):
    def flattenChild(self,node,child,next):
        current=child
        while current.next:
            if current.child:
                self.flattenChild(current,current.child,current.next)
            current=current.next
        node.next=child
        child.prev=node
        node.child=None
        current.next=next
        if next:
            next.prev=current
    def flatten(self, head):
        intial=head
        while intial:
            if intial.child:
                next_node=intial.next
                self.flattenChild(intial,intial.child,next_node)
            intial=intial.next
        return head




        