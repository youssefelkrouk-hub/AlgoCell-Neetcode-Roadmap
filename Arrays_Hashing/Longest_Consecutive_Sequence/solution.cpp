class Solution {
    public:
        int longestConsecutive(vector<int>& nums) {
            unordered_map<int,int> m ; 
            int rs = 0 ; 
            for( int i : nums ){
                if( !m[i] ){
                    int len = m[i-1] + m[i+1] +1 ; 
                    m[i] = len ; 
                    m[ i - m[i-1] ] = len ; 
                    m[ i + m[i+1] ] = len ; 
                    rs = max( rs , len ) ; 
                } 
            }
            return rs ; 
        }
    };