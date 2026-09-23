package Linked_List.Merge_Two_Sorted_Lists;

class Solution {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode rs = new ListNode(0) ; 
        ListNode curr = rs ; 
        while( list1 != null && list2 != null ){
            if( list1.val < list2.val ){
                curr.next = list1 ; 
                list1 = list1.next ; 
            }else {
                curr.next = list2 ; 
                list2 = list2.next ; 
            }
            curr = curr.next ; 
        }
        curr.next = list1 == null ? list2 : list1 ; 
        return rs.next ; 
    }
}