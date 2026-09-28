#include <iostream>
#include <vector>
class Solution {
    public:
        int helper( int start , int end , vector<int> &nums ){
            int n = (int) nums.size() ;
            vector<int> dp( n , 0 ) ; 
            dp[start] = nums[start] ; 
            dp[start+1] = nums[start+1] ; 
            dp[start+2] = nums[start] + nums[start+2] ;
            for( int i=start+3 ; i<=end; ++i ){
                dp[i] = nums[i] + max( dp[i-2] , dp[i-3] ) ; 
            } 
            return max( dp[end] , dp[end-1] ) ; 
        }
        int rob(vector<int>& nums) {
            int n = nums.size() ; 
            if( n <= 3 ){
                int rs = 0 ; 
                for( int i : nums ) rs = max( rs , i  ) ; 
                return rs ; 
            }else if( n==4 ){
                return max( nums[0] + nums[2] , nums[1] + nums[3] ) ; 
            }
            return max( helper( 0 , n-2 , nums ) , helper( 1 , n-1 , nums ) ) ;  
        }
    };