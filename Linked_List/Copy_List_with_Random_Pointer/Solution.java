package Linked_List.Copy_List_with_Random_Pointer;

import java.util.*;

class Solution {
    class Node {
        int val;
        Node next;
        Node random;

        public Node(int val) {
            this.val = val;
            this.next = null;
            this.random = null;
        }
    }

    public Node copyRandomList(Node head) {
        if( head == null ){
            return null ; 
        }
        Node curr = head ; 
        while ( curr != null ){
            Node l2 = new Node( curr.val ) ; 
            l2.next = curr.next ; 
            curr.next = l2 ; 
            curr = l2.next ; 
        }
        Node rs = head.next ; 
        curr = head ; 
        while( curr != null ){
            if( curr.random != null ){
                curr.next.random = curr.random.next ; 
            }
            curr = curr.next.next ;
        }
        curr = head ; 
        while ( curr != null ){
            Node l2 = curr.next ; 
            curr.next = curr.next.next ;
            curr = curr.next ; 
            if( curr != null ){
                l2.next = curr.next ; 
            } 
        }
        return rs ; 
    }
}