import java.util.* ; 
class Solution {
    public int[][] merge(int[][] intervals) {
        int n = intervals.length ; 
        Arrays.sort( intervals , 
            (a,b) -> a[0]-b[0]
        ); 
        List<int[]> inter = new ArrayList<>() ; 
        for( int i=0 ; i<n ; ++i ){
            int start = intervals[i][0] ; 
            int end = intervals[i][1] ; 
            while( i+1<n && intervals[i+1][0] <= end ){
                i++ ; 
                end = Math.max( end , intervals[i][1] ) ; 
            }
            inter.add( new int[]{ start , end }) ; 
        }
        int[][] rs = new int[inter.size()][] ; 
        for( int i=0 ; i<inter.size() ; ++i ){
            rs[i] = inter.get(i) ; 
        }
        return rs ; 
    }
}