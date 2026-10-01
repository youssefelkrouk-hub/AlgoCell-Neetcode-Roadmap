class Solution {
    public:
        int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
            int n = gas.size() ; 
            long long sum = 0 ; 
            for( int i=0 ; i<n ; ++i ){
                sum += ( gas[i] - cost[i] ) ; 
            }
            if( sum < 0 ) return -1 ; 
            long long pref = 0 ; 
            long long curr = 0 ; 
            int idx = 0 ; 
            for( int i=0 ; i<n ; ++i ){
                pref += ( gas[i] - cost[i] ) ; 
                if( pref < curr ){
                    curr = pref ; 
                    idx = i+1 ; 
                }
            }
            return idx ; 
        }
    };