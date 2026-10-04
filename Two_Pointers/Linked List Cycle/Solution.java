class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; next = null; }
}

public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;           // moves one step
            fast = fast.next.next;      // moves two steps
            if (slow == fast) return true;
        }
        return false;
    }
}