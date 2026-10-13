# definition of a single linked List :
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def middleNode(self,head):
        # define tow pointers , one is slow other is fast !!
        slow,fast=head,head
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next
        return slow