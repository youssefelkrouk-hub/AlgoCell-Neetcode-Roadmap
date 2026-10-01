class Solution {
    public:
        vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& inter) {
            vector<vector<int>> res ;
            int n = intervals.size() ; 
            for( int i=0 ; i<n ; ++i ){
                if( intervals[i][1] < inter[0] ){
                    res.push_back( intervals[i] ) ; 
                }else if( intervals[i][0] > inter[1] ){
                    res.push_back( inter ) ; 
                    while( i < n ){
                        res.push_back( intervals[i++] ) ; 
                    }
                    return res ; 
                }else{
                    inter[0] = min( inter[0] , intervals[i][0] ) ; 
                    inter[1] = max( inter[1] , intervals[i][1] ) ; 
                }
            }   
            res.push_back( inter ) ; 
            return res ; 
        }
    };