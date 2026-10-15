# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        temp=head
        stack=[]
        while temp:
            stack.append(temp)
            temp=temp.next
        # i use a stack because LIFO : last in the  stack i will compare it with the begining of the linked list and so on :

        temp=head
        while temp:
            if temp.val!=stack.pop().val:
                return False
            temp=temp.next
        return True 
        

        
        


        