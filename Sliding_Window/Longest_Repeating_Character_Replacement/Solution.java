class Solution {
    public int characterReplacement(String s, int k) {
        int n = s.length() ; 
        char[] chars = s.toCharArray() ; 
        if( k >= n-1 ){
            return n ; 
        }
        boolean[] fl = new boolean[128] ;
        for( char c : chars ){
            fl[c] = true ; 
        } 
        int rs = k+1 ; 
        for( int i=0 ; i<128 ; ++i ){
            if( !fl[i] ) continue ; 
            int count = 0 ; 
            int l = 0 ; 
            for( int j=0 ; j<n ; ++j ){
                if( chars[j] == i ) count++ ; 
                while( j - l + 1 - count > k ){
                   if( chars[l]  == i ) count-- ; 
                   l++ ; 
                }
                rs = Math.max( rs , j - l + 1 ) ; 
            }
        }
        return rs ;     
    }
}