class LinkedList(object):
    def __init__(self,x):
        self.val=x # stores the value you pass in
        self.next=None # no next yet 

class Solution:
    def hasCycle(self, head) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next # shifted by one 
            fast=fast.next.next # shifted by tow
            if slow is fast:
                return True
        return False



