class Solution {
    public String minWindow(String s, String t) {
        int n = s.length() ; 
        int m = s.length() ; 
        if( m > n ){
            return "" ; 
        }
        char[] chars = s.toCharArray() ; 
        int[] f = new int[128] ; 
        int count = 0 ; 
        for( char c : t.toCharArray() ){
            if( f[c]++ == 0 ) count++ ; 
        } 
        int rs = -1 ; 
        int start = 0 ; 
        int len = Integer.MAX_VALUE ; 
        for( int i=0 ; i<n ; ++i ){
            if( --f[ chars[i] ] == 0  ){
                count-- ; 
            }
            while( start<=i && f[ chars[start] ] < 0 ){
                f[ chars[start++] ]++ ;  
            }
            if( count == 0 && i - start + 1 < len ){
                rs = start ; 
                len = i - start + 1 ;
            }
        }
        return rs == -1 ? "" : s.substring( rs , rs + len ) ; 
    }
}