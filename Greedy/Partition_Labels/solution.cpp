class Solution {
    public:
        vector<int> partitionLabels(string s) {
            int n = s.size() ; 
            vector<int> m(26) ; 
            for( int i=0 ; i<n ; ++i ){
                m[ s[i] - 'a' ] = i ; 
            }
            vector<int> rs  ; 
            for( int i=0 ; i<n ; ++i ){
                int start = i ; 
                int end = m[ s[i] - 'a' ] ; 
                while( i < end ){
                    end = max( end , m[ s[i] - 'a' ] ); 
                    i++ ; 
                }
                rs.push_back( end - start + 1 ) ; 
            }
            return rs ; 
        }
    };