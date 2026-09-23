package Sliding_Window.Longest_Substring_Without_Repeating_Characters;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length() ; 
        int[] f = new int[128] ; 
        char[] chars = s.toCharArray() ; 
        int rs = 0 ; 
        int start = 0 ; 
        for( int i=0 ; i<n ; ++i ){
            f[ chars[i] ]++  ;
            while( f[ chars[i] ] > 1 ){
                f[ chars[start++] ]-- ; 
            }
            rs = Math.max( rs , i - start + 1 ) ; 
        }
        return rs ; 
    }
}