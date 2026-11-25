# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        temp=head
        List=[]
        while temp:
            List.append(temp)
            temp=temp.next
        # i will use a list to stocke all elment of the ll on it , and then operate a  tow pointers technique 

        l,r=0,len(List)-1
        while l<r:
            if List[l]!=List[r]:
                return False
            l+=1
            r-=1
        return True        