import java.util.*;

class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(
            (a,b) -> b-a
        ) ; 
        for( int stone : stones ){
            pq.offer( stone ) ; 
        }
        while( pq.size() > 1 ){
            int y = pq.poll() ; 
            int x = pq.poll() ; 
            if( x != y ){
                pq.offer( y - x ) ; 
            }
        }
        if( pq.size() == 1 ){
            return pq.peek() ; 
        }else { 
            return 0 ; 
        }
    }
}