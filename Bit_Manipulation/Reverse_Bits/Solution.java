class Solution {
    public int reverseBits(int n) {
        int rs = 0 ; 
        for( int i=0 ; i<32 ; ++i ){
            rs <<= 1 ; 
            if( (n&1) == 1 ){
                rs |= 1 ; 
            } 
            n >>= 1 ; 
        }
        return rs; 
    }
}