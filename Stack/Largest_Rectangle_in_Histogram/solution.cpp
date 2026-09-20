class Solution {
    public:
        int largestRectangleArea(vector<int>& heights) {
            int n = heights.size() ;
            int rs = 0 ; 
            vector<int> left(n) ; 
            vector<int> right(n) ;
            vector<int> s(n); 
            int in = -1 ; 
            for( int i=0 ; i<n ; ++i ){
                while( in != -1 && heights[s[in]] >= heights[i] ) {
                    in-- ; 
                }
                left[i] = in == -1 ? i+1 : i - s[in] ;
                s[++in] = i ;
            }
            in = -1 ; 
            for( int i=n-1 ; i>=0 ; --i ){
                while( in != -1 && heights[s[in]] >= heights[i] ) {
                    in-- ; 
                }
                right[i] = in == -1 ? n-i : s[in] - i ;
                s[++in] = i ; 
            }
    
            for( int i=0 ; i<n ; ++i ){
                rs = max( rs , (left[i] + right[i] - 1)*heights[i] ) ;
            }
            return rs ; 
        }
    };