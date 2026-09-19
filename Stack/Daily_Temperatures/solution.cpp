class Solution {
    public:
        vector<int> dailyTemperatures(vector<int>& temperatures) {
            int n = temperatures.size() ; 
            vector<int> st( n ) ; 
            int in = -1 ; 
            vector<int> rs( n , 0 ) ;
            for( int i=n-1; i>=0 ; --i ){
                while( in !=-1  && temperatures[ st[in] ] <= temperatures[i] ){
                    in-- ; 
                }
                if( in != -1 ){
                    rs[i] = st[in] - i ; 
                }
                st[++in] = i ;  
            }
            return rs ;  
        }
    };