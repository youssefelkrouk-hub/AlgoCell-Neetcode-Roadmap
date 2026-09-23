package Linked_List.Reorder_List;

 
class Solution {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    public void reorderList(ListNode head) {        
        ListNode slow = head , fast = head ; 
        while( fast != null && fast.next != null ){
            slow = slow.next ; 
            fast = fast.next.next ; 
        }
        ListNode curr = slow.next ; 
        slow.next = null ;  
        ListNode half = null ; 
        ListNode node = curr ; 
        while( node != null ){
            ListNode temp = node.next ; 
            node.next = half ; 
            half = node ; 
            node = temp ; 
        }
        node = head ; 
        while( half != null ){
            ListNode temp1 = node.next ; 
            ListNode temp2 = half.next ; 
            node.next = half ; 
            half.next = temp1 ; 
            node = temp1 ; half = temp2 ; 
        }
    }
}