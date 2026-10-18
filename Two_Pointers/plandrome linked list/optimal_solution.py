# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        fast,slow=head,head
        # Reach the midlle of the linked list
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # reverse the linked list from the middle into the end
        prev=None
        cur=slow
        while cur:
            tmp=cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        # verify if the linked list is palindrome
        # at the end of the while loop prev will point exactly in the end of linked list
        left,right=head,prev
        while right:
            if right.val != left.val:
                return False
            right=right.next
            left=left.next
        return True


            