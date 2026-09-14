class Solution {
    public:
        vector<vector<int>> threeSum(vector<int>& nums) {
            vector<vector<int>> res ; 
            int n = nums.size() ; 
            sort( nums.begin() , nums.end() ) ; 
            for( int i=0 ; i<n ; ++i ){
                if( nums[i] > 0 ) break ; 
                int l = i+1 ; 
                int r = n-1 ; 
                int target = -nums[i] ; 
                while( l < r ){
                    int sum = nums[l] + nums[r] ; 
                    if( sum < target ){
                        l++ ; 
                    }else if( sum > target ){
                        r-- ; 
                    }else {
                        vector<int> sol(3) ; 
                        sol[0] = nums[i] ;
                        sol[1] = nums[l] ;
                        sol[2] = nums[r] ;
                        res.push_back( sol ) ; 
                        while( l+1<r && nums[l+1] == nums[l] ) l++ ; 
                        l++ ; 
                        r-- ; 
                    }
                }
                while( i+1<n && nums[i+1] == nums[i] ) ++i ; 
            }
            return res ; 
        }
    };