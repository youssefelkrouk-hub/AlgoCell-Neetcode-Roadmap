# definition of a ListNode 


class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def return_the_begining(head):
        slow=fast=head
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None