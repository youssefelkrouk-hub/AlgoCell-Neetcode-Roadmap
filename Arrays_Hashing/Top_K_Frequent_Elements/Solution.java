import java.util.*;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int n = nums.length ; 
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a,b) -> a[1] - b[1]
        ); 
        int[] f = new int[2_0001] ;
        for( int i : nums ){
            f[ i + 1_0000 ]++ ; 
        }   
        for( int i=0 ; i<2_0001 ; ++i ){
            if( f[i] != 0 ){
                if( pq.size() < k ){
                    pq.add( new int[]{ i - 10000 , f[i] } ) ; 
                }else if( pq.peek()[1] < f[i] ){
                    pq.poll() ; 
                    pq.add( new int[]{ i - 10000 , f[i] } ) ; 
                }
            }
        }
        int[] rs = new int[k] ; 
        int in = 0 ;
        while( !pq.isEmpty() ){
            rs[in++] = pq.poll()[0] ; 
        } 
        return rs ; 
    }
}