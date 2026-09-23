# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(-1)
        curr = dummy 
        carry = 0 
        while l1 or l2 or carry : 
            a , b = 0 , 0 
            if l1 : 
                a = l1.val 
                l1 = l1.next 
            if l2 : 
                b = l2.val 
                l2 = l2.next 
            s = a + b + carry 
            curr.next = ListNode( s%10 ) 
            curr = curr.next 
            carry = 1 if s>9 else 0 
        return dummy.next  
        