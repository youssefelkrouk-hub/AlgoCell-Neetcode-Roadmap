class Solution {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
     
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode( -1 ) ; 
        int len = 0 ; 
        ListNode curr = head ; 
        while( curr != null ){
            len++ ; 
            curr = curr.next ; 
        }
        if( len < k ){
            return head ; 
        }
        int rounds = len/k ; 
        ListNode ele = head ; 
        ListNode tail = dummy ; 
        while( rounds-- > 0 ){
            ListNode nextTail = ele ; 
            ListNode rs = ele ; 
            ele = ele.next ; 
            for( int i=1 ; i<k ; ++i ){
                ListNode temp = ele.next ; 
                ele.next = rs ; 
                rs = ele ; 
                ele = temp ; 
            }
            nextTail.next = null ; 
            tail.next = rs ;
            tail = nextTail ; 
        } 
        tail.next = ele ; 
        return dummy.next ; 
    }
}