class Solution {
    public:
        vector<vector<int>> merge(vector<vector<int>>& intervals) {
            int n = intervals.size() ; 
            vector<vector<int>> rs  ; 
            sort( intervals.begin() , intervals.end() ) ; 
            for( int i=0 ; i<n ; ++i ){
                int start = intervals[i][0] ; 
                int end = intervals[i][1] ;
                while( i+1<n && intervals[i+1][0] <= end ){
                    i++ ; 
                    end = max( end , intervals[i][1] ) ; 
                }
                rs.push_back( {start,end} ) ; 
            } 
            return rs ; 
        }
    };