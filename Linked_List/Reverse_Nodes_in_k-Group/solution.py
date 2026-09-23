# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        l = 0  
        curr = head 
        while curr : 
            l += 1 
            curr = curr.next 
        rounds = l//k 
        dummy = ListNode(-1)
        ele = head 
        tail = dummy 
        while rounds : 
            rs = ele 
            nextTail = ele 
            ele = ele.next 
            for i in range(k-1) : 
                temp = ele.next 
                ele.next = rs 
                rs = ele
                ele = temp
            nextTail.next = None 
            tail.next = rs 
            tail = nextTail 
            rounds -= 1 

        tail.next = ele 
        return dummy.next 