package Sliding_Window.Permutation_in_String;

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int n = s1.length() ; 
        int m = s2.length() ; 
        if( m < n ){
            return false ; 
        }
        int[] f1 = new int[128] ; 
        for( char c : s1.toCharArray() ){
            f1[c]++ ;  
        }
        int[] curr = new int[128] ; 
        int start = 0 ; 
        int len = 0 ; 
        for( int i=0 ; i<m ; ++i ){
            int in = s2.charAt(i) ; 
            ++curr[in] ; 
            len++ ; 
            while( curr[in] > f1[in] ){
                --curr[ s2.charAt(start++) ] ; 
                len-- ; 
            } 
            if( len == n ) return true ; 
        }
        return false ; 
    }
}