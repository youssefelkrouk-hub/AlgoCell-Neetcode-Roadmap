class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
       curr = None
       while head : 
            temp = head.next 
            head.next = curr 
            curr = head 
            head = temp 
       return curr 