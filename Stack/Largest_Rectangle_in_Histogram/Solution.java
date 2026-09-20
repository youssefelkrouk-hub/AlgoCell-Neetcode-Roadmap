package Stack.Largest_Rectangle_in_Histogram;

class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length ; 
        int rs = 0 ; 
        int[] left = new int[n] ; 
        int[] right = new int[n] ;
        int[] s = new int[n] ; 
        int in = -1 ; 
        for( int i=0 ; i<n ; ++i ){
            while( in != -1 && heights[s[in]] >= heights[i] ){
                in-- ; 
            }
            left[i] = in == -1 ? i+1 : i - s[in] ; 
            s[++in] = i ; 
        }
        in = -1 ; 
        for( int i=n-1 ; i>=0 ; --i ){
            while( in != -1 && heights[s[in]] >= heights[i] ){
                in-- ; 
            }
            right[i] = in == -1 ? n-i : s[in] - i ; 
            s[++in] = i ; 
        }

        for( int i=0 ; i<n ; ++i ){
            rs = Math.max( rs , ( right[i] + left[i] - 1 )*heights[i] ) ; 
        } 
        return rs ;
    }
}