import java.util.*;

class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        int n = hand.length ; 
        if( n % groupSize !=0 ) return false ; 
        Map<Integer,Integer> m = new HashMap<>() ; 
        for( int i : hand ){
            m.put( i , m.getOrDefault(i,0)+1 ) ; 
        }
        Arrays.sort( hand ) ; 
        for( int i : hand ){
            if( m.get(i) > 0 ){
                for( int j=0 ; j<groupSize ; ++j ){
                    int curr = m.getOrDefault( i + j , 0 ) ; 
                    if( curr == 0 ){
                        return false; 
                    } 
                    m.put( i+j , curr-1 ) ; 
                }
            }
        }
        return true ; 
    }
}