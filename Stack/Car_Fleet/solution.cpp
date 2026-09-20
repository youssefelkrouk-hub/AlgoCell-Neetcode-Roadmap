class Solution {
    public:
        int carFleet(int target, vector<int>& position, vector<int>& speed) {
            int n = position.size() ; 
            int rs = 0 ; 
            vector< pair<int,int> > pairs( n ) ; 
            for( int i=0 ; i<n ; ++i ){
                pairs[i] = { position[i] , speed[i] } ; 
            }
            sort( pairs.rbegin() , pairs.rend() ) ; 
            double curr = 0 ; 
            for( int i=0 ; i<n ; ++i ){
                double inter = (double) ( target - pairs[i].first ) / pairs[i].second ; 
                if( inter > curr ){
                    rs++ ; 
                    curr = inter ; 
                }
            } 
            return rs ; 
        }
    };