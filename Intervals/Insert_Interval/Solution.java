import java.util.*;

class Solution {
    public int[][] insert(int[][] intervals, int[] inter ) {
        int n = intervals.length ; 
        ArrayList<int[]> res = new ArrayList<>() ; 
        for( int i=0 ; i<n ; ++i ){
            if(  inter[0] > intervals[i][1] ){
                res.add( intervals[i] ) ; 
            }else if( inter[1] < intervals[i][0] ){
                res.add(inter) ; 
                while( i<n ){
                    res.add(intervals[i]) ; 
                    i++ ; 
                }
                return  res.toArray( new int[res.size()][2] ) ; 
            }else {
                inter[0] = Math.min( inter[0] , intervals[i][0] ) ; 
                inter[1] = Math.max( inter[1] , intervals[i][1] ) ;  
            }
        }
        res.add(inter) ; 
        return res.toArray( new int[res.size()][2] ) ; 
    }
}