class LinkedList(object):
    def __init__(self,x):
        self.val=x # stores the value you pass in
        self.next=None # no next yet 

# the problem is the same as contain duplicate problem 
class Solution:
    def hasCycle(self, head) -> bool:
        seen=set()
        node=head
        while node:
            if node in seen:
                return True
            seen.add(node)
            node=node.next
        return False


