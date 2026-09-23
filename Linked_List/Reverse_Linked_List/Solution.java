package Linked_List.Reverse_Linked_List;

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode curr = null ;
        while( head != null ){
           ListNode temp = head.next ; 
           head.next = curr ; 
           curr = head ; 
           head = temp ; 
        }
        return curr ; 
    }
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
   
}


  