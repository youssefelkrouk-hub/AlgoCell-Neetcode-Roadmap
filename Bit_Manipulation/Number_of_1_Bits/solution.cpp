class Solution {
    public:
        int hammingWeight(int n) {
            int rs = 0 ; 
            while( n > 0 ){
                n -= n & -n  ; 
                rs++ ; 
            }
            return rs ; 
        }
    };