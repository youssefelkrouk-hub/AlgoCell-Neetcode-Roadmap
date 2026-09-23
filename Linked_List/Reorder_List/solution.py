# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reorderList(self, head):
        fast , slow = head , head 
        while fast and fast.next : 
            fast = fast.next.next 
            slow = slow.next 
        curr = slow.next 
        slow.next = None 
        half = None 
        while curr : 
            temp = curr.next 
            curr.next = half 
            half = curr 
            curr = temp 
        node = head
        while half :
            temp1 , temp2 = node.next , half.next
            node.next = half 
            half.next = temp1 
            node , half = temp1 , temp2