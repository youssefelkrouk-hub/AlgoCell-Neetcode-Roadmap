class Solution {
    public:
        bool canPartition(vector<int>& nums) {
           int n = nums.size() ; 
           if( n == 1 ) return false ; 
           int sum = 0 ; 
           for( int i : nums ) sum += i ; 
           if( sum % 2 == 1 ) return false ; 
           bitset<20'001> b ; 
           b[0] = 1 ; 
           for( int i : nums ){
                b |= ( b << i ) ; 
           }
           return b[sum/2];   
        }
    };