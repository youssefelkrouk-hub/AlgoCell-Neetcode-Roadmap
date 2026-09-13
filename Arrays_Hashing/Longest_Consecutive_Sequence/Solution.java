import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        HashMap<Integer,Integer> m = new HashMap<>() ; 
        int rs = 0 ; 
        for( int i : nums ){
            if( !m.containsKey(i) ){
                int len =  m.getOrDefault(i+1,0) + m.getOrDefault(i-1,0)+1 ; 
                m.put( i , len );
                m.put( i- m.getOrDefault(i-1,0) , len );
                m.put( i+ m.getOrDefault(i+1,0) , len );
                rs = Math.max( rs , len ) ; 
            }
        }
        return rs ; 
    }
}
