class Solution {
    public:
        int trap(vector<int>& height) {
            int n = height.size() ; 
            int l = 0 ; 
            int r = n-1 ; 
            int leftMax = height[0] ; 
            int rightMax = height[n-1] ; 
            int rs = 0 ; 
            while( l < r ){
                if( leftMax < rightMax ){
                    l++ ; 
                    leftMax = max( height[l] , leftMax ) ; 
                    rs += leftMax - height[l] ; 
                }else {
                    r-- ; 
                    rightMax = max( rightMax , height[r] ) ; 
                    rs += rightMax - height[r] ; 
                }
            }
            return rs ;
        }
    };