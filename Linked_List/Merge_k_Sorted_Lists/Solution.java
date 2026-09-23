import java.util.PriorityQueue;

class Solution {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode dummy = new ListNode(-1) ;
        ListNode curr = dummy ; 
        int k = lists.length ; 
        PriorityQueue<ListNode> pq = new PriorityQueue<>(
            (a,b) -> a.val - b.val
        ); 
        for( ListNode l : lists ){
            if( l != null ){
                pq.add(l) ; 
            }
        }
        while( !pq.isEmpty() ){
            ListNode ele = pq.poll() ; 
            curr.next = ele ; 
            if( ele.next != null ){
                pq.add( ele.next ) ; 
            }
            curr = curr.next ; 
        }
        return dummy.next ; 
    }
}