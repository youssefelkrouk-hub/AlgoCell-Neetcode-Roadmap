class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort( intervals , (a,b) -> a[0] - b[0] ) ; 
        int n = intervals.length ; 
        int prev = intervals[0][1] ; 
        int ans = 0 ; 
        for( int i=1 ; i<n ; ++i ){
            int start = intervals[i][0] ; 
            int end = intervals[i][1] ; 
            if( start >= prev ){
                prev = end ; 
            }else {
                ans++ ; 
                prev = Math.min( prev , end ) ; 
            }
        }
        return ans ; 
    }
}