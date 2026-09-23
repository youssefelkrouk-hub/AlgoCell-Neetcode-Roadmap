# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        right = head ; 
        left = head ; 
        while n > 0 : 
            right = right.next 
            n -= 1
    
        if not right  :
            return head.next; 

        while  right.next :
            right = right.next  
            left = left.next 
    
        left.next = left.next.next 
        return head 