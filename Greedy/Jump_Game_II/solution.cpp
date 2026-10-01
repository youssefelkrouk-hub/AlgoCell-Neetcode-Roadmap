class Solution {
    public:
        int jump(vector<int>& nums) {
            int n = nums.size() ; 
            if( n == 1 ) return 0 ;  
            int rs = 1 ; 
            int limit = nums[0] ; 
            int next = 0 ; 
            for( int i=0 ; i<n ; ++i){
                if( i <= limit ){
                    if( i + nums[i] > next ){
                        next = nums[i] + i ;
                    } 
                }else {
                    rs++ ; 
                    limit = next ; 
                    next = i + nums[i] ; 
                }
            }
            return rs ; 
        }
    };