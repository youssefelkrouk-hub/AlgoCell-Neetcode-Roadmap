class Solution {
    public:
        vector<int> topKFrequent(vector<int>& nums, int k) {
            int n = nums.size() ; 
            map<int,int> count ; 
            for( int i : nums ){
                count[i] = 1 + count[i] ; 
            }
            vector< vector<int> > inter(n+1 ) ;
            for( auto &p : count ){
                inter[ p.second ].push_back( p.first ) ; 
            } 
            vector<int> rs ; 
            for( int i=n ; i>=1 ; --i ){
                for( int j : inter[i] ){
                    rs.push_back( j ) ; 
                    if( rs.size() == k ) return rs ; 
                }
            }
            return rs ; 
        }
    };