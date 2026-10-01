class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int n = intervals.size() ; 
        sort( intervals.begin() , intervals.end() ) ; 
        int ans = 0 ; 
        int prev = intervals[0][1] ; 
        for( int i=1 ; i<n ; ++i ){
            int start = intervals[i][0] ; 
            int end = intervals[i][1] ; 
            if( start >= prev ){
                prev = end ; 
            }else {
                ans++ ;
                prev = min( prev , end ) ; 
            }
        }
        return ans ; 
    }
};