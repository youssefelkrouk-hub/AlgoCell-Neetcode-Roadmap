package Linked_List.Add_Two_Numbers;

class Solution {
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0) ; 
        ListNode curr = dummy ;
        int carry = 0 ; 
        while( l1 != null || l2 != null || carry != 0 ){
            int a=0 , b=0 ; 
            if( l1 != null ){
                a = l1.val ; 
                l1 = l1.next ; 
            }
            if( l2 != null ){
                b = l2.val ; 
                l2 = l2.next ; 
            }
            int sum = a+b+carry ; 
            curr.next = new ListNode( sum%10 ) ;
            curr = curr.next ; 
            carry = sum>9 ? 1 : 0 ; 
        }
        return dummy.next ; 
    }
}